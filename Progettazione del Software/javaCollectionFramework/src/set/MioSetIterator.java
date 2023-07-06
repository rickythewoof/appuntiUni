package set;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class MioSetIterator<E> implements Iterator<E> {

    private Node<E> curr;

    public MioSetIterator(Node<E> start){
        curr = start;
    }
    @Override
    public boolean hasNext() {
        return curr != null;
    }

    @Override
    public E next() {
        if(curr == null)
            throw new NoSuchElementException();
        E info = curr.info;
        curr = curr.next;
        return info;
    }
}
