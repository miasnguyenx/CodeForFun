import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        Queue<Person> personQueue = new LinkedList<>();
        personQueue.add(new Person("John Doe"));
        personQueue.add(new Person("Jane Smith"));
        personQueue.add(new Person("Alice Johnson"));
        personQueue.poll();
        ArrayList<Person> personList = new ArrayList<>();
        personList.add(new Person("John Doe"));
        personList.add(new Person("Jane Smith"));
        personList.add(new Person("Alice Johnson"));
        personList.remove(0);
        Stack<Person> personStack = new Stack<>();
        personStack.push(new Person("John Doe"));
    }
}
