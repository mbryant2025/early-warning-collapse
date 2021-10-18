#include <Arduino.h>
#include <WiFi.h>
#include <FirebaseESP32.h>
#include "time.h"
#include "addons/TokenHelper.h"
#include "addons/RTDBHelper.h"

#define WIFI_SSID "DukeVisitor"
#define WIFI_PASSWORD ""

#define API_KEY "AIzaSyAw3Q4yx8pN98zY9T_Ce8Rb0tex96uB6CI"
#define DATABASE_URL "early-warning-collapse-default-rtdb.firebaseio.com"

#define FLEX_SENSOR 34
#define FLEX_SENSOR_PATH "FlexSensor"

String device = "ESP1";
FirebaseData fbdo; 
FirebaseAuth auth; 
FirebaseConfig config; 
String databasePath = ""; 
String fuid = ""; 

const char* ntpServer = "pool.ntp.org";
const long  gmtOffset_sec = -18000;
const int   daylightOffset_sec = 3600;

unsigned long elapsedMillis = 0; 
unsigned long update_interval = 5000; 
bool isAuthenticated = false;

void Wifi_Init() {
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();
}

void firebase_init() {
  config.api_key = API_KEY;
  config.database_url = DATABASE_URL;
  Firebase.reconnectWiFi(true);
  Serial.println("------------------------------------");
  Serial.println("Sign up new user...");
  if (Firebase.signUp(&config, &auth, "", ""))
  {
    Serial.println("Success");
    isAuthenticated = true;
    databasePath = "/" + device;
    fuid = auth.token.uid.c_str();
  }
  else
  {
    Serial.printf("Failed, %s\n", config.signer.signupError.message.c_str());
    isAuthenticated = false;
  }
  config.token_status_callback = tokenStatusCallback;
  //Firebase.begin(&config, &auth);
}

void updateSensorValue(int sensorReading, String sensorName){
  Serial.println("------------------------------------");
  String node = databasePath + "/" + sensorName;
  if(Firebase.set(fbdo, node, sensorReading)){
    Serial.println("PASSED");
    Serial.print("VALUE: ");
    printResult(fbdo);
    Serial.println("------------------------------------");
    Serial.println();
  } else {
    Serial.println("FAILED");
    Serial.println("REASON: " + fbdo.errorReason());
    Serial.println("------------------------------------");
    Serial.println();
  }
}

String getTimeStamp(){
  struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    Serial.println("Failed to obtain time");
    return "Failed";
  }
  char timeStamp[100];
  strftime(timeStamp, 50, "%A, %B %d %Y %H:%M:%S", &timeinfo);
  return timeStamp;
}

void setup() {
  Serial.begin(115200);
  Wifi_Init();
  firebase_init();
  configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
}

void loop() {
  if(millis() - elapsedMillis > update_interval && isAuthenticated && Firebase.ready()){
    elapsedMillis = millis();
    int flexValue = analogRead(FLEX_SENSOR);
    updateSensorValue(flexValue, FLEX_SENSOR_PATH);
    Serial.println(getTimeStamp());
  }
}