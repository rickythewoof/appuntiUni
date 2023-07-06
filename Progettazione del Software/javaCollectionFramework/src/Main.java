import java.util.LinkedList;
import java.util.List;

import list.MiaLista;
import set.*;

public class Main {
    public String a;

    public static void main(String[] args) {

        List<String> l1 = new MiaLista<String>();
        l1.add("ciao");
        l1.add("come");
        l1.add("stai");

        System.out.println(l1);
        l1.clear();
        for (int i = 1; i <= 20; i++)
            l1.add(Integer.toString(i));

        System.out.println(l1);

        l1.add(1, "ciao");
        System.out.println(l1);
        System.out.println(l1.size());
    }
}