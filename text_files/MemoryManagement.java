/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package memorymanagement;

import java.util.ArrayList;
import java.util.Random;

class MemoryPage{
    private boolean U = false;
    private boolean M = false;

    public MemoryPage(boolean M, boolean U) {
        this.U = U;
        this.M = M;
    }
   
    public boolean getU(){
        return this.U;
    }
    
    public boolean getM(){
        return this.M;
    }
    
    public void setU(boolean newB){
        this.U = newB;
    }
    
    public void setM(boolean newB){
        this.M = newB;
    }
}
public class MemoryManagement {

    private static int pagesQuantity = 6;
    private static ArrayList<MemoryPage> pages = new ArrayList<MemoryPage>();
    
    public static void main(String[] args) {
            
        Random rand = new Random();
        for(int i = 0; i < pagesQuantity; i++) {
     
            rand.nextBoolean();
            pages.add(new MemoryPage(rand.nextBoolean(), rand.nextBoolean()));
        }
        
        for(MemoryPage pg : pages) {
            System.out.println("U: " + pg.getU() + "   M: " + pg.getM());
        }
        
        System.out.println("=============================");
        System.out.println("Number | Usage | Memory");
        System.out.println("=============================");
        
        int savepos = 0;
        
        while(true) { 
            int i = 1;
            
            int except = -1;
            
            boolean zero_one = false;
            boolean was = false;
            
            if(was == false) {
                zero_one = true;
            } else {
                
                zero_one = false;
            }
            
            for(int j = 0; j < pages.size(); j++) {
                
                System.out.print(i + "    |" +  pages.get(j).getU() + "     |" + pages.get(j).getM());
           
                if(zero_one) {
                    if((pages.get(j).getU() == false) && (pages.get(j).getM() == false)) {
                        System.out.println("  ++");
                        except = j;
                        resetAllU(except);
                    } else {
                        System.out.print("\n");
                    }
                    was = true;
                    
                } else if(!zero_one){ 
                    if(pages.get(j).getU() == false && pages.get(j).getM() == true) {
                        System.out.println(" ++");

                        except = j;
                        resetAllU(except);
                        was = false;
                    } else {
                        System.out.print("\n");
                    }
                } else {
                    System.out.print("\n");
                }  
        i++; 
    }
    
            System.out.println("=============================");
        
    }
    }
    
    public static void resetAllU(int exept) {
        for(int i = 0; i < pages.size(); i++) {
            
            if(i != exept) {
                pages.get(i).setU(false);
            } else {
                pages.get(i).setU(true);
            }
        }
    }
}
