#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <openssl/aes.h>
#include <openssl/evp.h>
#include <openssl/camellia.h>

#include <sys/types.h>
#include <sys/stat.h>

#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>

#include "key.h"
#include <time.h>


#define ITERATIONS 10000

typedef enum {
    AES_128_CBC,
    CAMELLIA_128_CBC,
    ARIA_128_CBC
} cipher_t;

unsigned char* encrypt(cipher_t mode, const unsigned char* key, const unsigned char* iv, const char* plaintext, int* out_len) {
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    if (!ctx) {
        perror("EVP_CIPHER_CTX_new");
        exit(1);
    }

    EVP_CIPHER* cipher = NULL;
    int BLOCK_SIZE = 0;

    switch(mode){
        case AES_128_CBC:
            cipher = EVP_aes_128_cbc();
            BLOCK_SIZE = AES_BLOCK_SIZE;
            break;
        case CAMELLIA_128_CBC:
            cipher = EVP_camellia_128_cbc();
            BLOCK_SIZE = CAMELLIA_BLOCK_SIZE;
            break;
        case ARIA_128_CBC:
            cipher = EVP_aria_128_cbc();
            BLOCK_SIZE = AES_BLOCK_SIZE;
            break;
    }
    if (EVP_EncryptInit_ex(ctx, cipher, NULL, key, iv) != 1) {
        perror("EVP_EncryptInit_ex");
        EVP_CIPHER_CTX_free(ctx);
        exit(1);
    }

    int plaintext_len = strlen(plaintext);
    int ciphertext_len = plaintext_len + BLOCK_SIZE;
    unsigned char* ciphertext = (unsigned char*)malloc(ciphertext_len);
    if (!ciphertext) {
        perror("malloc");
        EVP_CIPHER_CTX_free(ctx);
        exit(1);
    }

    int len;
    if (EVP_EncryptUpdate(ctx, ciphertext, &len, (unsigned char*)plaintext, plaintext_len) != 1) {
        perror("EVP_EncryptUpdate");
        free(ciphertext);
        EVP_CIPHER_CTX_free(ctx);
        exit(1);
    }
    ciphertext_len = len;

    if (EVP_EncryptFinal_ex(ctx, ciphertext + len, &len) != 1) {
        perror("EVP_EncryptFinal_ex");
        free(ciphertext);
        EVP_CIPHER_CTX_free(ctx);
        exit(1);
    }
    ciphertext_len += len;

    EVP_CIPHER_CTX_free(ctx);

    *out_len = ciphertext_len;
    return ciphertext;
}

unsigned char* decrypt(cipher_t mode, const unsigned char* key, const unsigned char* iv, const unsigned char* ciphertext, int ciphertext_len, int* out_len) {
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    if (!ctx) {
        perror("EVP_CIPHER_CTX_new");
        exit(1);
    }

    EVP_CIPHER* cipher = NULL;
    int BLOCK_SIZE = 0;
    switch(mode){
        case AES_128_CBC:
            cipher = EVP_aes_128_cbc();
            BLOCK_SIZE = AES_BLOCK_SIZE;
            break;
        case CAMELLIA_128_CBC:
            cipher = EVP_camellia_128_cbc();
            BLOCK_SIZE = CAMELLIA_BLOCK_SIZE;
            break;
        case ARIA_128_CBC:
            cipher = EVP_aria_128_cbc();
            BLOCK_SIZE = AES_BLOCK_SIZE;
            break;
    }

    if (EVP_DecryptInit_ex(ctx, cipher, NULL, key, iv) != 1) {
        perror("EVP_DecryptInit_ex");
        EVP_CIPHER_CTX_free(ctx);
        exit(1);
    }

    int plaintext_len = ciphertext_len;
    unsigned char* plaintext = (unsigned char*)malloc(plaintext_len + BLOCK_SIZE);
    if (!plaintext) {
        perror("malloc");
        EVP_CIPHER_CTX_free(ctx);
        exit(1);
    }

    int len;
    if (EVP_DecryptUpdate(ctx, plaintext, &len, ciphertext, ciphertext_len) != 1) {
        perror("EVP_DecryptUpdate");
        free(plaintext);
        EVP_CIPHER_CTX_free(ctx);
        exit(1);
    }
    plaintext_len = len;

    if (EVP_DecryptFinal_ex(ctx, plaintext + len, &len) != 1) {
        perror("EVP_DecryptFinal_ex");
        free(plaintext);
        EVP_CIPHER_CTX_free(ctx);
        exit(1);
    }
    plaintext_len += len;

    EVP_CIPHER_CTX_free(ctx);

    *out_len = plaintext_len;
    return plaintext;
}


int open_file(char* filename) {
    int fd = open(filename, O_RDONLY);
    if (fd == -1) {
        perror("open");
        exit(1);
    }
    return fd;
}

void* map_file(int fd) {
    struct stat st;
    if (fstat(fd, &st) == -1) {
        perror("fstat");
        exit(1);
    }
    void* memfile = mmap(NULL, st.st_size, PROT_READ, MAP_PRIVATE, fd, 0);
    if (memfile == MAP_FAILED) {
        perror("mmap");
        exit(1);
    }
    return memfile;
}
void benchmark_encryption_decryption(cipher_t mode, const char* plaintext, int plaintext_len, const unsigned char* key, const unsigned char* iv) {
    int ciphertext_len;
    double total_encryption_time = 0, total_decryption_time = 0;
    double max_encryption_time = 0, max_decryption_time = 0;
    double min_encryption_time = 1e9, min_decryption_time = 1e9;

    for (int i = 0; i < ITERATIONS; i++) {
        struct timespec start, end;

        clock_gettime(CLOCK_MONOTONIC, &start);
        unsigned char* ciphertext = encrypt(mode, key, iv, plaintext, &ciphertext_len);
        clock_gettime(CLOCK_MONOTONIC, &end);

        double encryption_time = (end.tv_sec - start.tv_sec) * 1e3 + (end.tv_nsec - start.tv_nsec) / 1e6;
        total_encryption_time += encryption_time;
        if (encryption_time > max_encryption_time) max_encryption_time = encryption_time;
        if (encryption_time < min_encryption_time) min_encryption_time = encryption_time;

        int decrypted_len;

        clock_gettime(CLOCK_MONOTONIC, &start);
        unsigned char* decrypted = decrypt(mode, key, iv, ciphertext, ciphertext_len, &decrypted_len);
        clock_gettime(CLOCK_MONOTONIC, &end);

        double decryption_time = (end.tv_sec - start.tv_sec) * 1e3 + (end.tv_nsec - start.tv_nsec) / 1e6;
        total_decryption_time += decryption_time;
        if (decryption_time > max_decryption_time) max_decryption_time = decryption_time;
        if (decryption_time < min_decryption_time) min_decryption_time = decryption_time;

        decrypted[decrypted_len] = '\0';

        if (strcmp(plaintext, (char*)decrypted) != 0) {
            fprintf(stderr, "Decrypted plaintext does not match original plaintext\n");
        }
        free(ciphertext);
        free(decrypted);
    }

    printf("Average encryption time: %.4f ms  (min %.4f ms  max %.4f ms)\n", total_encryption_time / ITERATIONS, min_encryption_time, max_encryption_time);
    printf("Average decryption time: %.4f ms  (min %.4f ms  max %.4f ms)\n", total_decryption_time / ITERATIONS, min_decryption_time, max_decryption_time);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    int fd = open_file(argv[1]);
    void* memfile = map_file(fd);

    char* plaintext = (char*)memfile;
    int plaintext_len = strlen(plaintext);

    printf("\n--------Benchmarking AES_128_CBC--------\n");
    benchmark_encryption_decryption(AES_128_CBC, plaintext, plaintext_len, KEY, IV);
    printf("\n--------Benchmarking CAMELLIA_128_CBC--------\n");
    benchmark_encryption_decryption(CAMELLIA_128_CBC, plaintext, plaintext_len, KEY, IV);
    printf("\n--------Benchmarking ARIA_128_CBC--------\n");
    benchmark_encryption_decryption(ARIA_128_CBC, plaintext, plaintext_len, KEY, IV);

    struct stat st;
    if (fstat(fd, &st) == -1) {
        perror("fstat");
        exit(1);
    }

    if (munmap(memfile, st.st_size)) {
        perror("munmap");
        exit(1);
    }
    close(fd);
    return 0;
}