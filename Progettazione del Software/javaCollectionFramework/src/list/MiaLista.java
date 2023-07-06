package list;

import java.util.*;

public class MiaLista<E> implements List<E>, Cloneable{
    private Object[] elems;
    private int size;

    public MiaLista(){
        elems = new Object[13];
        size = 0;
    }
    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public boolean contains(Object o) {
        for(int i = 0; i < size; i++)
            if(elems[i].equals(o)){
                return true;
            }
        return false;
    }

    @Override
    public Iterator<E> iterator() {
        return new MiaListaIterator<>(0, size, elems);
    }

    @Override
    public Object[] toArray() {
        return Arrays.copyOf(elems, size);
    }

    @Override
    public <T> T[] toArray(T[] ts) {
        return null;
    }       //TODO

    @Override
    public boolean add(E e) {
        if (this.size < elems.length){
            this.elems = Arrays.copyOf(elems, elems.length*2);
        }
        elems[size++] = e;
        return true;
    }

    @Override
    public boolean remove(Object o) {
        if(!contains(o))
            return false;
        else {
            while(contains(o)){
                remove(indexOf(o));
            }
            return true;
        }
    }


    @Override
    public boolean containsAll(Collection<?> collection) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean addAll(Collection<? extends E> collection) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean addAll(int i, Collection<? extends E> collection) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean removeAll(Collection<?> collection) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean retainAll(Collection<?> collection) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void clear() {
        this.size = 0;
        this.elems = new Object[13];

    }

    @Override
    public E get(int i) {
        if(size <= i)
            throw new IndexOutOfBoundsException();
        return (E) elems[i];
    }

    @Override
    public E set(int i, E e) {
        if(size <= i)
            throw new IndexOutOfBoundsException();
        E elem = (E) elems[i];
        elems[i] = e;
        return elem;

    }

    @Override
    public void add(int i, E e) {
        if (size+1 > elems.length){
            elems = Arrays.copyOf(elems, elems.length*2);
        }
        size++;
        for(int j = size-1; j > i; j--){
            elems[j] = elems[j-1];
        }
        elems[i] = (E) e;

    }

    @Override
    public E remove(int i) {
        if(i >= size)
            throw new IndexOutOfBoundsException();

        Object elem = elems[i];
        for (int j = i; j <size-1; j++){
            elems[j] = elems[j+1];
        }
        size--;
        if(elems.length < size*2){
            elems = Arrays.copyOf(elems, elems.length/2);
        }
        return (E) elem;
    }

    @Override
    public int indexOf(Object o) {
        if(!contains(o))
            return -1;
        else
            for(int i = 0; i < size; i++){
                if(elems[i].equals(o))
                    return i;
            }
            return 0;           //non arriverà mai lì
    }

    @Override
    public int lastIndexOf(Object o) {
        if(!contains(o))
            return -1;
        else
            for(int i = size-1; i >=0; i--){
                if(elems[i].equals(o))
                    return i;
            }
            return 0;
    }

    @Override
    public ListIterator<E> listIterator() {
        return (ListIterator<E>) new MiaListaIterator<>(0, size, elems);
    }

    @Override
    public ListIterator<E> listIterator(int i) {
        return (ListIterator<E>) new MiaListaIterator<>(i, size, elems);
    }

    @Override
    public List<E> subList(int i, int j) {
        if(i>size || j> size)
            throw new IndexOutOfBoundsException();
        MiaLista<E> res = new MiaLista<>();
        for(int r = i; r < j; r++)
            res.add(this.get(r));
        return res;
    }


    @Override
    public MiaLista<E> clone() {
        try {
            MiaLista res = (MiaLista) super.clone();
            res.size = this.size;
            res.elems = Arrays.copyOf(elems, elems.length);
            return res;
        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }
    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("[ ");
        for(E val : this) {
            sb.append(val.toString());
            sb.append(" ");
        }
        sb.append("]");
        return sb.toString();
    }
}
