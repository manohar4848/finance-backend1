from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from .permissions import RecordPermission


# GET + POST + FILTER
@api_view(['GET', 'POST'])
@permission_classes([RecordPermission])
def records_list(request):
    if request.method == 'GET':
        records = FinancialRecord.objects.all()

        # FILTERING
        type_param = request.GET.get('type')
        category = request.GET.get('category')
        date = request.GET.get('date')

        if type_param:
            records = records.filter(type=type_param)

        if category:
            records = records.filter(category=category)

        if date:
            records = records.filter(date=date)

        serializer = FinancialRecordSerializer(records, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = FinancialRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# GET ONE + UPDATE + DELETE
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([RecordPermission])
def record_detail(request, pk):
    try:
        record = FinancialRecord.objects.get(pk=pk)
    except FinancialRecord.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    if request.method == 'GET':
        serializer = FinancialRecordSerializer(record)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = FinancialRecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        record.delete()
        return Response({"message": "Deleted successfully"})


# DASHBOARD SUMMARY
@api_view(['GET'])
@permission_classes([RecordPermission])
def dashboard_summary(request):
    records = FinancialRecord.objects.all()

    total_income = sum(r.amount for r in records if r.type == 'income')
    total_expense = sum(r.amount for r in records if r.type == 'expense')

    return Response({
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense
    })


# CATEGORY SUMMARY
@api_view(['GET'])
@permission_classes([RecordPermission])
def category_summary(request):
    records = FinancialRecord.objects.all()
    data = {}

    for record in records:
        if record.category not in data:
            data[record.category] = 0
        data[record.category] += record.amount

    return Response(data)