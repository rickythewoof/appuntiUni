public class Tree {

    private int key;
    private Tree left;
    private Tree right;

    public Tree(int key) {
        this.key = key;
    }

    public static Tree build_1() {
        Tree n6 = new Tree(6);
        Tree n3 = new Tree(3);
        Tree n12 = new Tree(12);
        Tree n1 = new Tree(1);
        Tree n5 = new Tree(5);
        Tree n7 = new Tree(7);
        Tree n15 = new Tree(15);

        n6.left = n3;
        n6.right = n12;

        n3.left = n1;
        n3.right = n5;

        n12.left = n7;
        n12.right = n15;

        return n6;
    }

    public static Tree build_2() {
        Tree n6 = new Tree(6);
        Tree n3 = new Tree(3);
        Tree n12 = new Tree(12);
        Tree n1 = new Tree(1);
        Tree n5 = new Tree(5);
        Tree n7 = new Tree(7);
        Tree n15 = new Tree(15);

        n6.right = n3;
        n6.left = n12;

        n3.left = n1;
        n3.right = n5;

        n12.left = n7;
        n12.right = n15;

        return n6;
    }

    public static Tree build_3() {
        Tree n6 = new Tree(6);
        Tree n3 = new Tree(3);
        Tree n12 = new Tree(12);
        Tree n1 = new Tree(1);
        Tree n5 = new Tree(5);

        n6.left = n3;

        n3.left = n1;
        n3.right = n5;

        n5.right = n12;

        return n6;
    }

    public boolean isBST() {
        return isBST(this);
    }

    public boolean isBST(Tree t){
        if(t.left == null && t.right == null){
            return true;
        }
        else{
            if(t.left == null)
                if (t.key > t.right.key) return false;
                else return isBST(t.right);
            else if(t.right == null)
                if (t.key < t.left.key) return false;
                else return isBST(t.left);
            else
                if(t.left.key > t.key || t.right.key < t.key)   return false;
                else return isBST(t.left) && isBST(t.right);
        }
    }

    public boolean isBalanced() {
        return true;
    }

    public boolean isAVL() {
        return isBST(this) && (isAVL(this) <= Math.abs(1));
    }

    public int isAVL(Tree t){
        if(t.left == null && t.right == null){
            return 1;
        }
        if(t.left == null){
            return -1-isAVL(t.right);

        }if(t.right == null){
            return 1+isAVL(t.left);

        } return isAVL(t.left) - isAVL(t.right);
    }
}
