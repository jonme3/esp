#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Arteche Mobile";          // Nombre de la red WiFi
const char* password = "2017@Munguia";        // Contraseña de la red WiFi

void setup() {
  Serial.begin(115200);
  delay(1000);

  // Conectarse a la red WiFi
  WiFi.begin(ssid, password);
  Serial.println("Conectando a WiFi...");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.print("Conectado a WiFi con IP: ");
  Serial.println(WiFi.localIP());

  // Realizar una solicitud HTTP GET al servidor en Render
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin("https://esp-907c.onrender.com/esp32_connected"); // Endpoint correcto
    int httpCode = http.GET(); // Realizar la solicitud GET

    if (httpCode > 0) {
      Serial.printf("Código de respuesta: %d\n", httpCode);
      String payload = http.getString(); // Obtener la respuesta
      Serial.println(payload);           // Imprimir la respuesta en el monitor serie
    } else {
      Serial.println("Error al realizar la solicitud HTTP");
    }

    http.end();  // Finalizar la conexión HTTP
  }
}

void loop() {
  // Código adicional si lo necesitas
}
