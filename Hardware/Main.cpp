#include <SPI.h> 
#include <Adafruit_GFX.h> 
#include <Adafruit_ILI9341.h> 
 
#define cs 5 
#define dc 2 
#define rst 4 
 
Adafruit_ILI9341 tft = Adafruit_ILI9341(cs, dc, rst); 
String name = "Mateo"; 

//////////////////////////////////////////// Getting the Serial Value
int getSerialValue() {
  if (Serial.available()) {
    return Serial.parseInt();
  }

  return 0;
}

//////////////////////////////////////////// First Name Draw
void FirstNameQuestionDraw(){     
    tft.setTextSize(3); 
    tft.setTextColor(ILI9341_CYAN); 
    int x = 20; 
    int y = 85;  
    String text1 = "Welcome " + name + " how can i"; 
    String text2 = "assist you"; 
    for(int i = 0; i < text1.length(); i++){ 
        tft.setCursor(x,y); 
        tft.print(text1[i]); 
        x += 12;  
        delay(100);        
    } 
 
    x = 20;  
    y += 25;  
 
    for(int i = 0; i < text2.length(); i++){ 
        tft.setCursor(x,y); 
        tft.print(text2[i]); 
        x += 12;  
        delay(100);  
    } 
} 

//////////////////////////////////////////// Regular 
void RegNameQuestionDraw(){
    tft.setTextSize(3);
    tft.setTextColor(ILI9341_CYAN);
    int x = 20; 
    int y = 85; 
    String text1 = "How can i assist you";
    for(int i = 0; i < text1.length(); i++){
        tft.setCursor(x,y);
        tft.print(text1[i]);
        x += 12;
        delay(100);
    }
}

void setup(){ 
    Serial.begin(115200);
    tft.begin(); 
    tft.setRotation(1); 
    tft.fillScreen(ILI9341_BLACK);
 
} 
 
void loop(){ 
    int value = getSerialValue();
    if(value == 1){
        tft.fillScreen(ILI9341_BLACK);
        FirstNameQuestionDraw();
    }
    else if(value == 2){
        tft.fillScreen(ILI9341_BLACK);
        RegNameQuestionDraw();
    }
}