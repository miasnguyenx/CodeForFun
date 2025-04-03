public class Person {
    String name;
    String lastname;
    String firstname;
    int age;
    float balance;
    public Person(String name){
        this.name = name;
        this.lastname = name.split("")[1];
        this.firstname = name.split("")[0];
    }
    public Person(String lastname, String firstname){
        this.name = firstname + " " + lastname;
        this.lastname = lastname;
        this.firstname = firstname;
    }
    public static void main(String[] args) {
        Person person1 = new Person("John Doe");
        System.out.println("Name: " + person1.name);
        System.out.println("Last Name: " + person1.lastname);
        System.out.println("First Name: " + person1.firstname);
            
        Person person2 = new Person("Doe", "John");
        System.out.println("Name: " + person2.name);
        System.out.println("Last Name: " + person2.lastname);
        System.out.println("First Name: " + person2.firstname);
    }
}
