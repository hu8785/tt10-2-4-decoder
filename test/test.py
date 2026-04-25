import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start 2-4 Decoder Test")

    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    tests = [
        # A, B, E -> D0, D1, D2, D3
        ((0, 0, 0), (0, 1, 1, 1)),
        ((0, 0, 1), (1, 1, 1, 1)),
        ((0, 1, 0), (1, 0, 1, 1)),
        ((0, 1, 1), (1, 1, 1, 1)),
        ((1, 0, 0), (1, 1, 0, 1)),
        ((1, 0, 1), (1, 1, 1, 1)),
        ((1, 1, 0), (1, 1, 1, 0)),
        ((1, 1, 1), (1, 1, 1, 1)),
    ]

    for (A, B, E), (D0, D1, D2, D3) in tests:
        dut.ui_in[0].value = A
        dut.ui_in[1].value = B
        dut.ui_in[2].value = E

        await ClockCycles(dut.clk, 5)

        assert dut.uo_out[0].value == D0
        assert dut.uo_out[1].value == D1
        assert dut.uo_out[2].value == D2
        assert dut.uo_out[3].value == D3

    dut._log.info("2-4 Decoder Test Completed")
