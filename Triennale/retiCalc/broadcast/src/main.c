#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/select.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <errno.h>

#define PORT 12345
#define MAXRAND 16

typedef struct
{
    __u_short src;
    __u_short seq_num;
    __u_short data;
} Packet;

int main(int argc, const char **argv)
{

    setvbuf(stdout, NULL, _IONBF, 0);
    
    if (argc != 2)
    {
        printf("USAGE: ./node.o <num>\nGot %d args, for leader set num to 0\n", argc);
        exit(1);
    }

    int curr_seq = 0;
    int yes = 1;
    int ret, node_num = atoi(argv[1]), addr_len = sizeof(struct sockaddr_in);

    struct sockaddr_in brdc_addr;
    memset(&brdc_addr, 0, sizeof(struct sockaddr_in));

    brdc_addr.sin_family = AF_INET;
    brdc_addr.sin_addr.s_addr = htonl(INADDR_BROADCAST);
    brdc_addr.sin_port = htons(PORT);

    if (node_num == 0)
    {
        fprintf(stdout, "LEADER\n");
        fflush(stdout);
        // Socket creation
        int srv_sock = socket(AF_INET, SOCK_DGRAM, 0);
        if (srv_sock == -1)
        {
            perror("Error creating socket");
            exit(1);
        }

        ret = setsockopt(srv_sock, SOL_SOCKET, SO_BROADCAST, (char *)&yes, sizeof(yes));
        if (ret == -1)
        {
            perror("setsockopt error");
            return 0;
        }
        // TODO make server and bind
        struct sockaddr_in srv_addr;
        memset(&srv_addr, 0, sizeof(struct sockaddr_in));

        srv_addr.sin_family = AF_INET;
        srv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
        srv_addr.sin_port = htons(PORT);

        ret = bind(srv_sock, (struct sockaddr *)&srv_addr, (socklen_t)addr_len);

        sleep(10);

        int rand_num = rand() % MAXRAND, addr_len = sizeof(struct sockaddr_in);
        Packet packet = {.src = node_num, .seq_num = curr_seq, .data = rand_num};
        int to_send = sizeof(packet);
        ret = sendto(srv_sock, &packet, to_send, 0, (struct sockaddr *)&brdc_addr, (socklen_t)addr_len);
        if (ret == -1)
        {
            perror("Error sending broadcast!");
            exit(1);
        }
        fprintf(stdout, "Broadcast sent!\n");
    }
    else
    {
        fprintf(stdout, "CLIENT!\n");
        // Socket creation
        int cln_sock = socket(AF_INET, SOCK_DGRAM, 0);
        if (cln_sock == -1)
        {
            perror("Error creating socket");
            exit(1);
        }

        ret = setsockopt(cln_sock, SOL_SOCKET, SO_BROADCAST, (char *)&yes, sizeof(yes));
        if (ret == -1)
        {
            perror("setsockopt error");
            return 0;
        }
        fd_set readfd;

        FD_ZERO(&readfd);
        FD_SET(cln_sock, &readfd);
        ret = select(cln_sock + 1, &readfd, NULL, NULL, 0);
        if (ret > 0)
        {
            if (FD_ISSET(cln_sock, &readfd))
            {
                int to_read = sizeof(Packet);
                Packet packet = {};
                ret = recvfrom(cln_sock, &packet, to_read, 0, NULL, NULL);
                if (ret == -1)
                {
                    perror("error on recv!");
                    exit(1);
                }
                fprintf(stdout, "[Node #%d] Received message %d from node %d", node_num, packet.data, packet.src);
                if (packet.src != curr_seq && packet.seq_num > curr_seq)
                {
                    int to_write = sizeof(Packet);
                    while (to_write > 0)
                        ret = sendto(cln_sock, &packet, to_write, 0, (struct sockaddr *)&brdc_addr, (socklen_t)addr_len);
                    if (ret == -1)
                    {
                        perror("error sending back!");
                        exit(1);
                    }
                    fprintf(stdout, "Sent back to broadcast!\n");
                }
                else
                {
                    fprintf(stdout, "Discarting...\n");
                }
            }
        }
    }
    return 0;
}