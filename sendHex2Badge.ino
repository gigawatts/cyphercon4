/* Cyphercon 4.0 Badge tape emulator by Gigawatts
 * Any Arduino compatible microcontroller with 3 volt logic levels should work.
 * I used a TI Stellaris LaunchPad LM4F120 with Energia, thus the strange pin names.
 * This should work fine with a 3 volt Arduino Uno, just update the pin numbers.
 * 
 * 
 * Instructions: Open up a serial terminal to your microcontroller at 115200 baud.
 * Use the "punch-tape-decoder.html" web page to decode your punch tape to hex.
 * Paste the hex codes generated into your serial terminal, followed by a carriage return.
 * The serial terminal should echo back your hex input and your badge should blink away.
 */

//setting up Punch Hole pins
const int holeOne = PD_6;   //Least Signficant bit  //Top of Badge, Right most on badge LEDs
const int holeTwo = PB_7;   //
const int holeThree = PB_6; //
const int holeClock = PF_3; //Green LED  //Small hole, clock signal
const int holeFour = PB_3;  //
const int holeFive = PC_4;  //
const int holeSix = PC_5;   //
const int holeSeven = PC_6; //Most Significant bit
const int holeEight = PC_7; //Parity bit  //Bottom of Badge, Left most on badge LEDs
const int power = PB_2;

//array of holes in MSB to LSB order
int holes[] = { holeEight, holeSeven, holeSix, holeFive, holeFour, holeThree, holeTwo, holeOne };

#define ZERO_PADDING 8

void setup() {
  pinMode(power, OUTPUT);
  pinMode(holeClock, OUTPUT);
  pinMode(holeOne, OUTPUT);
  pinMode(holeTwo, OUTPUT);
  pinMode(holeThree, OUTPUT);
  pinMode(holeFour, OUTPUT);
  pinMode(holeFive, OUTPUT);
  pinMode(holeSix, OUTPUT);
  pinMode(holeSeven, OUTPUT);
  pinMode(holeEight, OUTPUT);
  Serial.begin(115200);
  
  digitalWrite(power, HIGH);
}

// Main loop #############################################################
void loop()
{
    static char buffer[1024];
    static size_t length = 0;

    if (Serial.available()) {
        char c = Serial.read();

        // On carriage return, process the received data.
        if (c == '\r') {
            Serial.println();

            // Properly terminate the string.
            buffer[length] = '\0';

            // Convert the hex data to a byte array.
            size_t byte_count = length/2;
            uint8_t data[byte_count];
            hex2bin(data, buffer, &byte_count);

            // Echo back the byte array in hex.
            Serial.print("Hex input: ");
            for (size_t i = 0; i < byte_count; i++) {
                Serial.print(data[i], HEX);
                Serial.print(" ");
            }
            Serial.println();

            // Echo back the byte array in binary and send to badge
            Serial.print("Sending Binary bits to Badge...  ");
            
            for (size_t i = 0; i < byte_count; i++) {
                //Serial.println( ZeroPadBin(data[i]) );  // print each row of binary output

                // Send data bits first
                binToLeds( ZeroPadBin(data[i]) );

                // Then light up the clock bit, wait a bit, and turn it off
                sendClock(10);

                // Then turn all the data bits off, wait for a while, loop to next row
                blankLeds();
                delay(20);
            }
            Serial.println("Done!");

            // Reset the buffer for next line.
            length = 0;
        }

        // Otherwise buffer the incoming byte.
        else if (length < sizeof buffer - 1) {
            //Serial.write(c);  // echo out input characters
            buffer[length++] = c;
        }
    }
}

// Functions ##################################################################
/*
 * Convert an hex string to binary. Spaces are allowed between bytes.
 * The output array is supposed to be large enough.
 * On return, *size is the size of the byte array.
 */
static void hex2bin(uint8_t *out, const char *in, size_t *size){
    size_t sz = 0;
    while (*in) {
        while (*in == ' ') in++;  // skip spaces
        if (!*in) break;
        uint8_t c = *in>='a' ? *in-'a'+10 : *in>='A' ? *in-'A'+10 : *in-'0';
        in++;
        c <<= 4;
        if (!*in) break;
        c |= *in>='a' ? *in-'a'+10 : *in>='A' ? *in-'A'+10 : *in-'0';
        in++;
        *out++ = c;
        sz++;
    }
    *size = sz;
}

// Add leading zeros to a binary number
String ZeroPadBin(uint8_t number){
  char binstr[]="00000000";
  uint8_t i=0;
  uint16_t n=number;
     while(n>0 && i<ZERO_PADDING){
        binstr[ZERO_PADDING-1-i]=n%2+'0';
        ++i;
        n/=2;
     } 
     //Serial.print(binstr);
     return binstr;
}

// Send a binary string to the badge
void binToLeds(String binary_string){
  for (int x = 0; x < 8; x++) {
    digitalWrite(holes[x], (binary_string.charAt(x) == '0' ? LOW : HIGH));
  }
}

// Send a clock high then low signal
void sendClock(int pause){
  digitalWrite(holeClock, HIGH);
  delay(pause);
  digitalWrite(holeClock, LOW);
}

// Blank all inputs
void blankLeds(){
  for( int x = 0; x < 8; x++ ) {
    digitalWrite(holes[x], LOW);
  }
}
