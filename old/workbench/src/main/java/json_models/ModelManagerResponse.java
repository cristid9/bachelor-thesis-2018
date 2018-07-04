package json_models;

import lombok.Data;

import java.util.List;

@Data
public class ModelManagerResponse {
    public List<List<Integer>> comparators;
}
