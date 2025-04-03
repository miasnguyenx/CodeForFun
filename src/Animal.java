public class Animal {
    String name;
    String species;
    int age;
    float weight;
    public Animal(String name){
        this.name = name;
        this.species = "Unknown";
        this.age = 0;
        this.weight = 0.0f;
    }
    public Animal(String name, String species){
        this.name = name;
        this.species = species;
        this.age = 0;
        this.weight = 0.0f;
    }
    public Animal(String name, String species, int age, float weight){
        this.name = name;
        this.species = species;
        this.age = age;
        this.weight = weight;
    }
}
