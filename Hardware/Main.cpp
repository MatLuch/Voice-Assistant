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
    int ammDots = 0;

    while(!Serial.available()){
        tft.setTextSize(3);
        tft.setTextColor(NeonGreen, ILI9341_BLACK);
        int x = 45;
        int y = 100;

        String displayText = "Listening";

        for(int i = 0; i < ammDots; i++){
            displayText += ".";
        }

        while(displayText.length() < 12){
            displayText += " ";
        }

        tft.setCursor(x,y);
        tft.print(displayText);
        
        ammDots++; 

        if(ammDots > 3){
            ammDots = 0; 
        }

        delay(500);
    }
}

//////////////////////////////////////////// Procesing Draw
void ProcessingDraw(){
    tft.setTextSize(3);
    tft.setTextColor(ILI9341_CYAN);
    String displayText = "Processing: ";

    int centerX = 45;
    int centerY = 100; 
    int radius = 40; 
    int pushFactor = 100;

    int positionsX[8] = {160, 188, 200, 188, 160, 132, 120, 132};
    int positionsY[8] = {80, 92, 120, 148, 160, 148, 120, 92};

    int dot = 0; 

    tft.setCursor(10, 105);
    tft.print(displayText);

    while(!Serial.available()){

        for(int i = 0; i < 8; i++){
            tft.fillCircle(positionsX[i] + pushFactor, positionsY[i], 5, ILI9341_DARKGREY);
        }

        tft.fillCircle(positionsX[dot] + pushFactor, positionsY[dot], 5, NeonGreen);

        dot++; 

        if(dot >= 8){
            dot = 0; 
        }

        delay(100);
        tft.fillCircle(250, 120, 45, ILI9341_BLACK);
    }    
}

//////////////////////////////////////////// Sentence Draw
void SentenceDraw(String text){
    tft.setTextSize(2);
    tft.setTextColor(NeonPink);
    int x = 10;
    int y = 50; 

        for(int i = 0; i < text.length(); i++){
            if(!Serial.available()){
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
        else if(value[0] == '4'){
            tft.fillScreen(ILI9341_BLACK);
            ProcessingDraw();
        }
    }

    else if(value.length() > 1){
        tft.fillScreen(ILI9341_BLACK);
        SentenceDraw(value);
    }
}