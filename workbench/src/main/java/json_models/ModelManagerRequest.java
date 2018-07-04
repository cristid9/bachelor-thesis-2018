package json_models;

import lombok.Data;

@Data
public class ModelManagerRequest {
    public String modelType;
    public int numberOfWires;
}
