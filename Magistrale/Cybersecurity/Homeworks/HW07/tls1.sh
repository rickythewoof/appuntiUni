#!/bin/bash

# List of websites to test
websites=(
    "google.com"
    "corriere.it"
    "facebook.com"
    "github.com"
    "amazon.it"
    "stackoverflow.com"
    "twitter.com"
    "aruba.it"
    "libero.it"
    "repubblica.it"
    "senato.it"
    "ny.org"
)

# Function to test TLS handshake time
test_tls_handshake() {
    local website=$1
    echo "Testing TLS handshake for $website..."

    # Run s_client to initiate TLS handshake and capture time
    time echo | openssl s_client \
        -connect "$website":443 \
        -servername "$website" \
	-brief -tls1_1
}

# Loop through all the websites
for website in "${websites[@]}"; do
    test_tls_handshake "$website"
done
