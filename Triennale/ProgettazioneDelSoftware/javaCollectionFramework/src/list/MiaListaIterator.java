package list;

import java.util.Iterator;

public class MiaListaIterator<E> implements Iterator<E> {

    private int index;
    private int size;
    private Object[] list;

    public MiaListaIterator(int i, int size, Object[] list){
        index = i;
        this.size = size;
        this.list = list;
    }

    @Override
    public boolean hasNext() {
        if(index < size)
            return true;
        else
            return false;
    }

    @Override
    public E next() {
        if(this.list == null)
            throw new NullPointerException();
        return (E) list[index++];
    }
}
