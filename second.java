import java.util.*;
import java.util.stream.*;

public class second {
    public static void main(String[] args) {
        List<Employee> employees = Arrays.asList(
            new Employee("Alice", 25, 50000),
            new Employee("Bob", 35, 60000),
            new Employee("Charlie", 28, 70000),
            new Employee("David", 30, 40000),
            new Employee("Eve", 22, 55000)
        );
        List<Employee> filtered = employees.stream()
            .filter(employee -> employee.getAge() <= 30)
            .collect(Collectors.toList());
        List<Employee> sorted = filtered.stream()
            .sorted(Comparator.comparing(Employee::getSalary).reversed())
            .collect(Collectors.toList());
        double totalSalary = sorted.stream()
            .mapToDouble(Employee::getSalary).sum();
        Optional<Employee> highest= sorted.stream().findFirst();

        System.out.println("Filtered Employees: " + filtered);
        System.out.println("Sorted Employees: " + sorted);
        System.out.println("Total Salary: " + totalSalary);
        highest.ifPresent(employee -> 
            System.out.println("Employee with Highest Salary: " + employee.getName())
        );
    }
}

class Employee {
    private String name;
    private int age;
    private double salary;

    public Employee(String name, int age, double salary) {
        this.name = name;
        this.age = age;
        this.salary = salary;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public double getSalary() {
        return salary;
    }

    @Override
    public String toString() {
        return "Employee{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", salary=" + salary +
                '}';
    }
}
