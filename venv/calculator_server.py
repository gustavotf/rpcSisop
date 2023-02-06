from calculator_pb2_grpc import CalculatorServicer

from calculator_pb2 import SumRequest
from calculator_pb2 import SumReply
from calculator_pb2 import MultiplyRequest
from calculator_pb2 import MultiplyReply
from calculator_pb2 import LargestRequest
from calculator_pb2 import LargestReply
from calculator_pb2 import DivisionRequest
from calculator_pb2 import DivisionReply

from grpc import ServicerContext


class Calculator(CalculatorServicer):

    def Sum(self, request: SumRequest, context: ServicerContext) -> SumReply:
        return SumReply(s=request.a + request.b)

    def Multiply(self, request: MultiplyRequest, context: ServicerContext) -> MultiplyReply:
        return MultiplyReply(s=request.a * request.b)

    def Largest(self, request: LargestRequest, context: ServicerContext) -> LargestReply:
        return LargestReply(s=request.a if request.a>request.b and request.a>request.c else (request.b if request.b>request.a and request.b>request.c else request.c))

    def Division(self, request: DivisionRequest, context: ServicerContext) -> DivisionReply:
        return DivisionReply(s=int(request.a / request.b), s1=int(request.a % request.b))
