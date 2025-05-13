import javax.swing.JApplet;

public class Heap {
    
    private HeapEntry[] heapList; 
    HEAP_TYPE type;
    private int nextNode = 0; 
    public enum HEAP_TYPE {MAX_HEAP, MIN_HEAP};

    public static class HeapEntry {
        int key;
        int value;
        protected HeapEntry(int k, int v) {key = k; value = v;}
    }

    public Heap(HEAP_TYPE type, int capacity) {
        this.type = type; 
        heapList = new HeapEntry[capacity];
    }

    public HEAP_TYPE getType() {
        return type;
    }

    public int peek() {
        return heapList[0].key;
    }

    public boolean isValid(int i){
        if( i < heapList.length && i >= 0  && heapList[i] != null) return true;
        else return false;
    }

    public boolean exchange(int i, int j){
        if (isValid(i) && isValid(j)){
            HeapEntry temp = heapList[j];
            heapList[j] = heapList[i];
            heapList[i] = temp;
            return true;
            }
        else return false;
    }

    protected int parent (int j) { return (j-1) / 2;}
    protected int left (int j) { return 2*j + 1;}
    protected int right (int j) { return 2*j + 2;}
    protected boolean hasLeft(int j) {return left(j) < size();}
    protected boolean hasRight(int j) {return right(j) < size();}

    private void downHeap(int j){
        int down = j;
        while (hasLeft(down)){
            int index = left(down);
            if(hasRight(down) && (heapList[right(down)].key < heapList[left(down)].key) )
                index = right(down);

            System.out.println("CHANGE " + down + " TO " + index);
            if(heapList[down].key <= heapList[index].key)
                break;
            exchange(down, index);
            down = index;
        }
    }
    
    private void upHeap(int j){
        int up = j;
        while(heapList[up].key < heapList[parent(up)].key){
            exchange(up, parent(up));
            up = parent(up);
        }
    }

    public HeapEntry add(int key) {
        HeapEntry newHeap = new HeapEntry(key, key);
        if(getType().equals(HEAP_TYPE.MIN_HEAP)){
            heapList[nextNode] = newHeap;
            upHeap(nextNode);
            nextNode++;
        }
        else {
            System.out.println("SUCA");
        }
        return newHeap;
    }

    public int getEntryKey(HeapEntry e) {
        return e.key;
    }

    public int size() {
        return nextNode;
    }

    public int poll() {
        int res = peek();
        heapList[0] = heapList[nextNode-1];
        downHeap(0);
        nextNode --;
        return res;
    }

    public static Heap array2heap(int[] array, HEAP_TYPE type) {
        Heap newHeap = new Heap(type, array.length);
        int start = newHeap.parent(array.length-1);
        for (int i = start; i >= 0; i--){
              newHeap.downHeap(i);
        }
        return newHeap;
    }

    public void print() {
        for (int i = 0; i < size(); i++ )
            System.out.print(" " + getEntryKey(heapList[i]));
        System.out.println();
    }

    public static void heapSort(int[] array) {
        Heap heap = array2heap(array, HEAP_TYPE.MIN_HEAP);
        for (int i = 0; i < array.length; i++){
            array[i] = heap.poll();
        }
    }

    public void updateEntryKey(HeapEntry e, int key) {
        return;
    }

}
