package set;
import java.lang.reflect.Array;
import java.util.Collection;
import java.util.Iterator;
import java.util.Set;

@SuppressWarnings("unused")
public class MioSet<E> implements Set<E>, Cloneable{

    Node<E> start;

    public MioSet() {
        start = null;
    }

    @Override
    public int size() {
        int i = 0;
        Node<E> node = start;
        while (node != null) {
            node = node.next;
            i++;
        }
        return i;
    }


    @Override
    public boolean isEmpty() {
        return start == null;
    }

    @Override
    public boolean contains(Object o) {
        for (Node<E> node = start; node != null; node = node.next) {
            if (node.info == o)
                return true;
        }
        return false;
    }

    @Override
    public Iterator<E> iterator() {
        return new MioSetIterator<>(start);
    }

    @Override
    public Object[] toArray() {
        Object[] res = new Object[this.size()];
        Node<E> node = start;
        for(int i = 0; i < size(); i++){
            res[i] = node.info;
            node = node.next;
        }
        return res;
    }

    @Override
    @SuppressWarnings("unchecked")
    public <T> T[] toArray(T[] ts) {
        //UTILIZZA METODO DELLA REFLECTION
        T[] res = (T[]) Array.newInstance(ts.getClass().getComponentType(), size());
        int i = 0;
        for(Node<E> node = start; node != null; node = node.next){
            res[i++] = (T) node.info;
        }
        return res;
    }

    @Override
    public boolean add(E e) {
        if (!contains(e)) {
            Node<E> newNode = new Node<E>(e);
            Node<E> node = start;
            if (node == null) {
                start = newNode;
            } else {
                while (node.next != null)
                    node = node.next;
                node = newNode;
            }
            return true;
        } else
            return false;
    }

    @Override
    public boolean remove(Object o) {
        if (!contains(o))
            return false;
        else {
            if (start.info.equals(o)) {
                start = start.next;
                return true;
            } else {
                Node<E> node = start;
                Node<E> nextNode = start.next;
                while (nextNode != null) {
                    if (nextNode.info.equals(o)) {
                        node.next = nextNode.next;
                        return true;
                    }
                    node = node.next;
                    nextNode = nextNode.next;
                }
            }
        }
        return false;
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
    public boolean retainAll(Collection<?> collection) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean removeAll(Collection<?> collection) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void clear() {
        start = null;
    }

    @Override
    public boolean equals(Object o){
        if(o!= null | !getClass().equals(o.getClass()))
            return false;
        MioSet<E> other = (MioSet<E>) o;
        for(Node<E> node = start; node != null; node = node.next){
            if(!other.contains(node.info))
                return false;
        }
        return size() == other.size();
    }
    @Override
    public int hashCode(){
        int res = 0;
        for (E info : this)
            res+=info.hashCode();
        return res;
    }

    @Override
    public MioSet<E> clone() {
        try {
            MioSet<E> clone = (MioSet<E>) super.clone();
            if(size()>0){
                Node<E> newStart = new Node<E>(start.info, start.next);
                Node<E> copyIter = newStart;
                for(Node<E> node = start; node != null; node = node.next){
                    copyIter.next = new Node<>(node.info, node.next);
                    copyIter = copyIter.next;
                }
                clone.start = newStart;
            }
            return clone;
        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }

    @Override
    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("( ");
        for(E elem : this) {
            sb.append(elem.toString());
            sb.append(" ");
        }
        sb.append(")");
        return sb.toString();
    }
}