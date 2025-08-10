package weatherforecast;



// HTTP request (REST API protocol) - POST / GET / PUT / DELETE
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

// HTTP response (is made up of JSON inside.), this package is for reading the actual content of information we get.
import com.google.gson.JsonObject;
import com.google.gson.JsonArray;
import com.google.gson.JsonParser;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;


import java.nio.file.Files; // for recording JSON response
import java.nio.file.Paths;
import java.nio.file.Path;
import java.io.IOException;



public class WeatherAPITest {
    public static void main(String[] args) {
        String apiKey = "2960a6f138614352816224807250908"; // Replace with your actual API key
        String city = "Atlanta";
        String url = String.format("https://api.weatherapi.com/v1/forecast.json?key=%s&q=%s&days=3&aqi=no&alerts=no", apiKey, city);


        OkHttpClient client = new OkHttpClient(); // abstraction of ourselves (You requesting)
        Request request = new Request.Builder().url(url).build(); // a letter for the request

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) throw new RuntimeException("Unexpected code " + response);
            String body = response.body().string();

            JsonObject json = JsonParser.parseString(body).getAsJsonObject();

            Gson gson = new GsonBuilder()
                    .setPrettyPrinting()  // enable indentation
                    .create();

            // Write to file
            try {
                Files.writeString(Paths.get("forecast.json"), gson.toJson(json));
                System.out.println("Saved forecast to forecast.json");
            } catch (IOException e) {
                e.printStackTrace();
            }





            System.out.println("Weather forecast for " + city + ":");




            JsonArray forecastDays = json.getAsJsonObject("forecast").getAsJsonArray("forecastday");

            for (int i = 0; i < forecastDays.size(); i++) {
                JsonObject dayData = forecastDays.get(i).getAsJsonObject();
                String date = dayData.get("date").getAsString();
                JsonObject day = dayData.getAsJsonObject("day");
                double maxTemp = day.get("maxtemp_c").getAsDouble();
                double minTemp = day.get("mintemp_c").getAsDouble();
                String condition = day
                        .getAsJsonObject("condition")
                        .get("text")
                        .getAsString();

                System.out.println(date + " -> " + condition + ", Max: " + maxTemp + "°C, Min: " + minTemp + "°C");
            }

            ////////////////////////////////
            /// HW3
            /// Do your own research what to do in the app, and 
            /// try to process the json so you can get the info you 
            /// need for the functionalities.
            /// 
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}