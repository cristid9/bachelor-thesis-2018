console.log("Initializing the core graphics...");

var main = function () {

    var container = document.getElementById("draw_area_core");
    var paper = Raphael(container, 200, 300);
    
    var draw_network = function(num_wires, comparators) {
        console.log("Core SN drawer called...");
        var wire_y_offset = 5;
        var network_x_offset = 10;

        for (var i = 0; i < num_wires; ++i) {
            var line = paper.path( ["M", "10", 10 + i * 10, "L", 
                wire_y_offset * Math.pow(num_wires, 2), 10 + i * 10]);
        }        

        for (var j = 0; j < comparators.length; ++j) {
            var line = paper.path( ["M", network_x_offset * 5, comparators[j][0] * 10 + 10, "L", 
                network_x_offset * 5, comparators[j][1] * 10 + 10] );
        
            network_x_offset++;
        }
    
    };

    // test
    draw_network(6, [[0, 1], [1, 2], [2, 3], [1, 5]]);
};

