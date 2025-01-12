#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <errno.h>
#include <ifaddrs.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/stat.h>

#define GENERATOR_FIFO_NAME "generator"
#define ANALYZER_FIFO_NAME "analyzer"
int src_num, seq_num;



int generator_pipe;
int analyzer_pipe;

typedef struct Payload
{
    int value;
} Payload;

typedef struct Message
{
    int source;
    int sequence;
    int payload_lenght;
    Payload* payload;
} Message;

Message *prepare_message(Payload *payload);

//---------------
// Traffic Generator
//---------------

// Some sistem that triggers handler callback every x milliseconds

void generator_function(){
    
}


//---------------
// Broadcaster
//---------------

Message *prepare_message(Payload *payload)
{
    Message *msg = calloc(1, sizeof(Message));
    msg->source = src_num;
    msg->sequence = seq_num;
    msg->payload_lenght = sizeof(int);
    msg->payload = payload;

    return msg;
}

typedef void (*BroadcasterHandler)(void *broadcaster, Payload *payload);

typedef struct Broadcaster
{
    // .. Local data to manage broadcast
    // e.g. socket opened, network interfaces,
    // sequence of other nodes...
    int sock_fd;
    struct sockaddr_in *addr;
    socklen_t size_sockaddr;
    int seq_sent;

    BroadcasterHandler handler;
} Broadcaster;

void register_handler(Broadcaster *broadcaster, BroadcasterHandler handler)
{
    broadcaster->handler = handler;
}

void send_broadcast(Broadcaster *broadcaster, Payload *payload)
{

    int ret = sendto(broadcaster->sock_fd, payload, sizeof(Payload), 0, (struct sockaddr*) broadcaster->addr, broadcaster->size_sockaddr);
    if (ret == -1)
    {
        perror("Error sending payload!");
        exit(1);
    }
}

void process_broadcaster(Broadcaster *broadcaster)
{
    // In case of packet reception, notify the handler
    // Discard already seen packets

    // TODO pipe to traffic 
}

//---------------
// Traffic Analyzer
//---------------

typedef struct TrafficHead{
    TrafficAnalyzer* first;
    TrafficAnalyzer* last;
} TrafficHead;

typedef struct TrafficAnalyzer
{
    int node_id;
    time_t datetime;
    struct TrafficAnalyzer* next;

} TrafficAnalyzer;

void analyzer_function(){
    analyzer_pipe = open(ANALYZER_FIFO_NAME, O_RDONLY);
    if(analyzer_pipe < 0){
        perror("Error opening analyzer pipe");
        exit(1); 
    }
    TrafficHead head = {.first = NULL, .last = NULL};

}

TrafficAnalyzer* push_to_queue(TrafficHead* head, TrafficAnalyzer* analyzer){
    assert(head != NULL && analyzer != NULL);

    if(head->first == NULL){
        head->first = analyzer;
        analyzer->next = NULL;
        head->last = analyzer;
    } else {
        TrafficAnalyzer* last = head->last;
        last->next = analyzer;
        head->last = analyzer;
    }

    return analyzer;
}

TrafficAnalyzer* pop_from_queue(TrafficHead* head){
    assert(head!=NULL);
    if(head->first == NULL){
        return NULL;
    }
    TrafficAnalyzer* popped = head->first;
    head->first = popped->next;

    return popped;
}

int peek_time_from_first(TrafficHead* head){
    assert(head!=NULL && head->first != NULL);
    return head->first->datetime;
}

void received_pkt(TrafficHead *head, int source)
{
    TrafficAnalyzer* analyzer = calloc(1,sizeof(TrafficAnalyzer));
    analyzer->node_id = source;
    analyzer->datetime = time(NULL);
    push_to_queue(head, analyzer);

}

void dump(TrafficHead *head);
{
    // Dump information about the thoughput of all packets received
}

//-------------------------
// Utility
// ------------------------

/**
 * Bind the given socket to all interfaces (one by one)
 * and invoke the handler with same parameter
 */
void bind_to_all_interfaces(int sock, void *context, void (*handler)(int, void *))
{
    struct ifaddrs *addrs, *tmp;
    getifaddrs(&addrs);
    tmp = addrs;
    while (tmp)
    {
        if (tmp->ifa_addr && tmp->ifa_addr->sa_family == AF_PACKET)
        {
            setsockopt(sock, SOL_SOCKET, SO_BINDTODEVICE, tmp->ifa_name, sizeof(tmp->ifa_name));
            handler(sock, context);
        }
        tmp = tmp->ifa_next;
        
    }
    freeifaddrs(addrs);
}

/**
 * Sleep a given amount of milliseconds
 */
int msleep(long msec)
{
    struct timespec ts;
    int res;

    if (msec < 0)
    {
        errno = EINVAL;
        return -1;
    }

    ts.tv_sec = msec / 1000;
    ts.tv_nsec = (msec % 1000) * 1000000;

    do
    {
        res = nanosleep(&ts, &ts);
    } while (res && errno == EINTR);

    return res;
}

int main()
{
    //Broadcaster on main!
    //TODO open pipe brdc->nlyz
    //               gnrt->brdc


    // Autoflush stdout for docker
    setvbuf(stdout, NULL, _IONBF, 0);


    // Traffic generator
    
    pid_t generator_pid = fork();
    
    switch(generator_pid){
        case(-1):
            perror("Fork() failed");
            return -1;
        case(0):
            //TODO: 
            //  - Enable traffic generator
            generator_function();
            break;
        default:
            generator_pipe = open(GENERATOR_FIFO_NAME, O_WRONLY);
            if(generator_pipe < 0){
                perror("Error opening pipe");
                exit(1);
            }
            break;
    }
    // Traffic analyzer
    pid_t analyzer_pid = fork();
    switch(analyzer_pid){
        case(-1):
            perror("Fork() failed");
            return -1;
        case(0):
            //TODO: 
            //  - Enable traffic analyzer
            analyzer_function();
            break;
        default:
            break;
    }
}