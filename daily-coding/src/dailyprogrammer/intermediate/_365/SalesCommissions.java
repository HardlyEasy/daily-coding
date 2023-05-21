package dailyprogrammer.intermediate._365;

import java.io.*;
import java.net.URL;
import java.util.HashMap;
import java.util.ArrayList;

public class SalesCommissions {
    static final double COMMISSION_RATE = .062;

    public static void main(String[] args) {
        HashMap<String, ArrayList<Product>> hm =
                new HashMap<String, ArrayList<Product>>();
        readFile(hm);
        for (String person : hm.keySet()) {
            double commission = calcCommission(hm.get(person));
            System.out.printf("%8s : $%.2f\n", person, commission);
        }
    }
    // Calculates total commission
    public static double calcCommission(ArrayList<Product> products) {
        double commission = 0;
        for (Product p : products) {
            double profit = p.getRevenue() - p.getExpense();
            if (profit >= 0) // Commission allowed only on profits
                commission += profit * COMMISSION_RATE;
        }
        return commission;
    }

    // Reads csv file data into a hashmap mapping person to products
    public static void readFile(HashMap<String, ArrayList<Product>> hm) {
        URL url = SalesCommissions.class.getResource("sales.csv");
        try {
            FileReader fr = new FileReader(url.getPath());
            BufferedReader br = new BufferedReader(fr);
            String lineStr = "";
            String splitter = ",";
            while ((lineStr = br.readLine()) != null) {
                String[] lineList = lineStr.split(splitter);
                Product product = new Product(lineList[1],
                        Integer.parseInt(lineList[2]),
                        Integer.parseInt(lineList[3]));
                String personName = lineList[0];
                if (!hm.containsKey(personName)) // Initialize hashmap entry
                    hm.put(personName, new ArrayList<Product>());
                hm.get(personName).add(product);
            }
        } catch (IOException exc) {
            System.out.println(exc);
        }
    }
} // end class SalesCommissions


class Product {
    private String name;
    private int revenue;
    private int expense;
    public Product(String name, int revenue, int expense) {
        this.name = name;
        this.revenue = revenue;
        this.expense = expense;
    }
    public String getName() {
        return name;
    }
    public int getRevenue() {
        return revenue;
    }
    public int getExpense() {
        return expense;
    }
    public String toString() {
        return name + "," + Integer.toString(revenue) + "," +
                Integer.toString(expense);
    }
}

class Person {
    private String name;
    private ArrayList<Product> products;
    public Person(String name, ArrayList<Product> products) {
        this.name = name;
        this.products = products;
    }
    public String getName() {
        return name;
    }
    public ArrayList<Product> getProducts() {
        return products;
    }
    public void addProduct(Product p) {
        this.products.add(p);
    }
}