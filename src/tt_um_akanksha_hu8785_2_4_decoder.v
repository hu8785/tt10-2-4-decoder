`default_nettype none

module tt_um_akanksha_hu8785_2_4_decoder (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    wire A = ui_in[0];
    wire B = ui_in[1];
    wire E = ui_in[2];

    wire [3:0] D;

    assign D[0] = ~(~A & ~B & ~E);
    assign D[1] = ~(~A &  B & ~E);
    assign D[2] = ~( A & ~B & ~E);
    assign D[3] = ~( A &  B & ~E);

    assign uo_out[0] = D[0];
    assign uo_out[1] = D[1];
    assign uo_out[2] = D[2];
    assign uo_out[3] = D[3];
    assign uo_out[4] = 1'b0;
    assign uo_out[5] = 1'b0;
    assign uo_out[6] = 1'b0;
    assign uo_out[7] = 1'b0;

    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    wire _unused = &{ena, clk, rst_n, ui_in[7:3], uio_in, 1'b0};

endmodule

`default_nettype wire
