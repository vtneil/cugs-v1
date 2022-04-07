#define SERIAL_BAUD 115200
unsigned long int counter = 1;

String team_id = "SPARK2";
String mission_time = "10:00:00";
String device_id = "Juno";
String mode = "F";

unsigned int state = 1;
float gps_alt = 0.0;
float bar_alt = 1.0;
float imu_alt = -3.0;

float temp1 = 25.0;
float temp2 = 35.0;

float batt_volt = 7.4;
String gps_time = "10:00:01";
float gps_lat = 13.001001;
float gps_lon = 100.001001;
unsigned int gps_sats = 26;

float acc_x = 0.68;
float ang_x = 2.56;
String cmd_echo = "";

String packet = "";

void setup() {
    Serial.begin(SERIAL_BAUD);
}

void loop() {
    packet = team_id;
    packet += "," + mission_time;
    packet += "," + String(counter++);
    packet += "," + device_id;
    packet += "," + mode;
    packet += "," + String(state);
    packet += "," + String(gps_alt += 0.01, 2);
    packet += "," + String(bar_alt += 0.01, 2);
    packet += "," + String(imu_alt += 0.01, 2);
    packet += "," + gps_time;
    packet += "," + String(gps_lat += 0.00001, 6);
    packet += "," + String(gps_lon += 0.00001, 6);
    packet += "," + String(gps_sats);
    packet += "," + String(temp1 += 0.01, 2);
    packet += "," + String(temp2 += 0.01, 2);
    packet += "," + String(acc_x += 0.01, 2);
    packet += "," + String(acc_x += 0.01, 2);
    packet += "," + String(acc_x += 0.01, 2);
    packet += "," + String(ang_x += 0.1, 2);
    packet += "," + String(ang_x += 0.1, 2);
    packet += "," + String(ang_x += 0.1, 2);
    packet += "," + String(batt_volt += 0.1, 2);
    packet += "," + cmd_echo;

    Serial.println(packet);
    delay(1000);
}
