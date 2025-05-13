import matplotlib.pyplot as plt

# Data from the output
domains = [
    "google.com", "corriere.it", "facebook.com", "github.com", 
    "stackoverflow.com", "aruba.it", 
    "libero.it", "repubblica.it", "senato.it"
]
real_times = [
    0.071, 0.119, 0.056, 0.083, 0.038, 0.101, 0.098, 
    0.045, 0.153
]
tls_versions = [
    "TLSv1.3", "TLSv1.2", "TLSv1.3", "TLSv1.3", "TLSv1.3", 
    "TLSv1.2", "TLSv1.2", "TLSv1.3", "TLSv1.2"
]

# Combine the domain and TLS version into a label for each domain
labels = [f"{domain}\n({tls})" for domain, tls in zip(domains, tls_versions)]

# Create a histogram
plt.figure(figsize=(10, 6))
plt.barh(labels, real_times, color='skyblue')

# Labels and title
plt.xlabel('Real Time (s)', fontsize=12)
plt.ylabel('Domain and TLS Version', fontsize=12)
plt.title('TLS Handshake Real Time', fontsize=14)

# Show the plot
plt.tight_layout()
plt.show()
