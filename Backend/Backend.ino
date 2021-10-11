#include <WiFi.h>
#include "aWOT.h"
#include "StaticFiles.h"

#define WIFI_SSID "DukeOpen"
#define WIFI_PASSWORD ""
#define LED_BUILTIN 2
#define FLEX_SENSOR 4

WiFiServer server(80);
Application app;
bool ledOn;

void setup() {
  Serial.begin(115200);

  pinMode(LED_BUILTIN, OUTPUT);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(WiFi.localIP());

  app.get("/led", &readLED);
  app.put("/led", &updateLED);
  
  app.use(staticFiles());
  server.begin();
}

void loop() {
  WiFiClient client = server.available();

  if (client.connected()) {
    app.process(&client);
  }
}

void updateLED(Request &req, Response &res) {
  ledOn = (req.read() != '0');
  digitalWrite(LED_BUILTIN, ledOn);
  return readLED(req, res);
}

void readLED(Request &req, Response &res){
  res.print(ledOn);
}
