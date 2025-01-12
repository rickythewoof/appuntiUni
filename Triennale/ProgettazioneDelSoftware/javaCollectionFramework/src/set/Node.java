package set;

class Node<E> {
    E info;
    Node<E> next;

    public Node(E info){
        this(info, null);
    }
    public Node(E info, Node<E> next) {
        this.info = info;
        this.next = next;
    }
}
