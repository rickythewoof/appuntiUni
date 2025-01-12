import random
import subprocess

num_nodes = 10
project_directory = "./src"
image = None

# Return a random connected graph n nodes and n-1 edges 
def get_random_edges(num_nodes):

    partition = dict((i, [i]) for i in range(num_nodes))

    def pair_random(max):
        a = random.randint(0, max-1)
        while True:
            b = random.randint(0, max-1)
            if a != b:
                return (a, b) if a < b else (b, a)
            
    edges = []

    while len(partition.keys()) > 1:
        keys = list(partition.keys())
        a, b = pair_random(len(keys))
        a = keys[a]
        b = keys[b]
        edges.append((partition[a][0], partition[b][0]))
        partition[a] = partition[a] + partition[b]
        del partition[b]

    return edges

# Get yaml file for a n equal containers connected 
# according a specific set of edges
def get_yaml(num_nodes, edges):
    buffer = "services:\n"
    for node in range(num_nodes):
        buffer += f"\tnode{node}:\n"

        if image:
            buffer += f"\t\timage: {image}\n"
        else:
            buffer += "\t\tbuild:\n"
            buffer += f"\t\t\tcontext: {project_directory}\n"
            buffer += "\t\t\tdockerfile: Dockerfile\n"

        params = [f"'{node}'"]
        params = ", ".join(params)
        buffer += f"\t\tcommand: [{params}]\n"

        buffer += "\t\tnetworks:\n"
        for edge in edges:
            if node in edge:
                buffer += f"\t\t- edge_{edge[0]}_{edge[1]}\n"
    buffer += "networks:\n"
    for edge in edges:
        buffer += f"\tedge_{edge[0]}_{edge[1]}:\n"

    buffer = buffer.replace("\t", "  ")
    return buffer

with open("compose.yaml", "w+") as file:
    file.write(get_yaml(num_nodes, get_random_edges(num_nodes)))

cmd = "docker compose up --build"

result = subprocess.run(cmd.split(" "), stderr=subprocess.PIPE)

print(result.stderr.decode('utf-8'))









