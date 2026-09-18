// code for my hardware
#include <SPI.h> 
#include <Adafruit_GFX.h> 
#include <Adafruit_ILI9341.h> 
 
#define cs 5 
#define dc 2 
#define rst 4 

#define NeonGreen 0x3FE2
#define NeonPink  0xF81F

Adafruit_ILI9341 tft = Adafruit_ILI9341(cs, dc, rst); 
String name = "Mateo"; 

//////////////////////////////////////////// Getting the Serial Value
String getSerialValue() {
  if (Serial.available()) {
    return Serial.readStringUntil('\n');
  }

  return "";
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

//////////////////////////////////////////// Regular Name Draw
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

//////////////////////////////////////////// Listening Draw
void ListeningDraw(){
    tft.setTextSize(3);
    tft.setTextColor(NeonGreen, ILI9341_BLACK);
    int x = 45;
    int y = 100;

    for(int i = 0; i < 10; i++){
        tft.setCursor(x, y);       
        String displayText = "Listening";
        int dots = i % 4; 
        for(int d = 0; d < dots; d++){
            displayText += ".";
        }
        while(displayText.length() < 12) {
            displayText += " ";
        }
        tft.print(displayText);
        delay(500);
    }
}

//////////////////////////////////////////// Sentence Draw
void SentenceDraw(String text){
    tft.setTextSize(2);
    tft.setTextColor(NeonPink);
    int x = 10;
    int y = 50; 

    for(int i = 0; i < text.length(); i++){
        tft.setCursor(x,y);
        tft.print(text[i]);

        x += 12; 

        if(x > 300){
            x = 10; 
            y += 20; 
        }
        delay(100);
    }
}

/////////////////////////////////////////////////////////////////// The setup and loop
void setup(){ 
    Serial.begin(115200);
    tft.begin(); 
    tft.setRotation(1); 
    tft.fillScreen(ILI9341_BLACK);
 
} 
 
void loop(){ 
    String value = getSerialValue();
    value.trim();

    if(value.length() == 1){
        if(value[0] == '1'){
            tft.fillScreen(ILI9341_BLACK);
            FirstNameQuestionDraw();
        }
        else if(value[0] == '2'){
            tft.fillScreen(ILI9341_BLACK);
            RegNameQuestionDraw();
        }
        else if(value[0] == '3'){
            tft.fillScreen(ILI9341_BLACK);
            ListeningDraw();
        }
    }

    else if(value.length() > 1){
        tft.fillScreen(ILI9341_BLACK);
        SentenceDraw(value);
    }
}