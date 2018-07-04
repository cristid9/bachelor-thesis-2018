package com.sorting_network_web_ui.demo;

import json_models.ModelManagerRequest;
import json_models.ModelManagerResponse;
import org.codehaus.jackson.map.ObjectMapper;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.net.SocketException;
import java.net.SocketTimeoutException;
import java.net.UnknownHostException;

public class ManagerClient {

    public static final String HOST_ADDRESS = "localhost";
    public static final int HOST_PORT = 2018;
    public static final int TIMEOUT = 3000;

    private String packReuqest(ModelType modelType, int numOfWires) {
        ObjectMapper objectMapper = new ObjectMapper();

        ModelManagerRequest request = new ModelManagerRequest();
        request.setModelType(modelType.name());
        request.setNumberOfWires(numOfWires);

        try {
            return objectMapper.writeValueAsString(request) + "\n";
        } catch (IOException e) {
            return null;
        }
    }

    private ModelManagerResponse unpackResponse(String rawResponse) {
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            ModelManagerResponse response = objectMapper.readValue(rawResponse, ModelManagerResponse.class);
            return response;
        } catch (IOException e) {
            return null;
        }
    }

    public ModelManagerResponse queryModelManager(ModelType modelType, int numberOfWires) {

        try {
            @SuppressWarnings("resource")
            Socket client = new Socket(HOST_ADDRESS, HOST_PORT);
            client.setSoTimeout(TIMEOUT);

            DataOutputStream outToServer = new DataOutputStream(client.getOutputStream());
            BufferedReader inFromServer = new BufferedReader(new InputStreamReader(client.getInputStream()));

            outToServer.writeBytes(packReuqest(modelType, numberOfWires));
            String modedInput = inFromServer.readLine();
            client.close();
            return unpackResponse(modedInput);

        } catch(SocketTimeoutException e) {
            System.out.println("Timed Out Waiting for a Response from the Server");
        } catch (SocketException e) {
            e.printStackTrace();
        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        return null;
    }
}
