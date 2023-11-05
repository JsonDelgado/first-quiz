package org.velezreyes.quiz.question6;

public class DrinkImplements implements Drink{
	private String name;
    private boolean fizzy;

    private int cost;

    public DrinkImplements(String name, boolean fizzy, int cost) {
        this.name = name;
        this.fizzy = fizzy;
        this.cost = cost;
    }
    @Override
    public String getName() {
        return name;
    }
    @Override
    public boolean isFizzy() {
        return fizzy;
    }
    public int getCost() {
        return this.cost;
    }


}
