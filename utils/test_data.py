"""Separate module to handle framework test data"""
from attrdict import AttrDict


def load_test_data():
    test_data_dict = {
        'STEP_PAYMENT': AttrDict({"CARDINAL_URL": "/?myBillAmount=&myBillName=&myBillEmail=&myBillTel=&errorcode=0&transactionreference=42-14-119&baseamount=1000&currencyiso3a=GBP&errormessage=Payment+has+been+successfully+processed&settlestatus=0&jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NjExMDk1MDQsInBheWxvYWQiOnsicmVxdWVzdHJlZmVyZW5jZSI6Ilc0Mi1hZncxa2didSIsImp3dCI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUpwYzNNaU9pSnNhWFpsTWw5aGRYUnZhbmQwSWl3aWFXRjBJam94TlRZMU16UTJOVE01TGpjNE9UZ3dNVGdzSW5CaGVXeHZZV1FpT25zaVltRnpaV0Z0YjNWdWRDSTZJakV3TURBaUxDSmhZMk52ZFc1MGRIbHdaV1JsYzJOeWFYQjBhVzl1SWpvaVJVTlBUU0lzSW1OMWNuSmxibU41YVhOdk0yRWlPaUpIUWxBaUxDSnphWFJsY21WbVpYSmxibU5sSWpvaWRHVnpkREVpTENKc2IyTmhiR1VpT2lKbGJsOUhRaUo5ZlEuN3VWYUdkQkhJQjFQZ196aTBBOE9ZbVIwb0NfWWJaOGp0YWVSUXgxWXQtRSIsInZlcnNpb24iOiIxLjAwIiwicmVzcG9uc2UiOlt7InRyYW5zYWN0aW9uc3RhcnRlZHRpbWVzdGFtcCI6IjIwMTktMDQtMTkgMDg6MDg6MjIiLCJsaXZlc3RhdHVzIjoiMSIsImlzc3VlciI6IlBVQkxJQyBCQU5LIEJFUkhBRCIsInNldHRsZWR1ZWRhdGUiOiIyMDE5LTA0LTE5IiwiZXJyb3Jjb2RlIjoiMCIsInRpZCI6IjI3ODg3NzU2IiwibWVyY2hhbnRudW1iZXIiOiI5ODk2NTMyNSIsInNlY3VyaXR5cmVzcG9uc2Vwb3N0Y29kZSI6IjAiLCJ0cmFuc2FjdGlvbnJlZmVyZW5jZSI6IjQyLTE0LTExOSIsIm1lcmNoYW50bmFtZSI6IkxpdmUgVW5pdHRlc3QgU2l0ZSA8PiYhXy09K0AjOjssLi8_T0siLCJwYXltZW50dHlwZWRlc2NyaXB0aW9uIjoiTUFTVEVSQ0FSRCIsImJhc2VhbW91bnQiOiIxMDAwIiwiYWNjb3VudHR5cGVkZXNjcmlwdGlvbiI6IkVDT00iLCJhY3F1aXJlcnJlc3BvbnNlY29kZSI6IjAwIiwicmVxdWVzdHR5cGVkZXNjcmlwdGlvbiI6IkFVVEgiLCJzZWN1cml0eXJlc3BvbnNlc2VjdXJpdHljb2RlIjoiMiIsImN1cnJlbmN5aXNvM2EiOiJHQlAiLCJhdXRoY29kZSI6IjUiLCJlcnJvcm1lc3NhZ2UiOiJPayIsIm9wZXJhdG9ybmFtZSI6ImxpdmUyX2F1dG9qd3QiLCJtZXJjaGFudGNvdW50cnlpc28yYSI6IkdCIiwibWFza2VkcGFuIjoiNTIwMDAwIyMjIyMjMDAwNyIsInNlY3VyaXR5cmVzcG9uc2VhZGRyZXNzIjoiMCIsImlzc3VlcmNvdW50cnlpc28yYSI6Ik1ZIiwic2V0dGxlc3RhdHVzIjoiMCJ9XSwic2VjcmFuZCI6Im1jNFQwd2dQVUEwTlByIn19.ypZyN2CMwn9q4niUeERIgHDR2ISQAtp0otpCXIUPoow",
                                "VISA_SUCCESS_URL": "/?myBillAmount=&myBillName=&myBillEmail=&myBillTel=&errorcode=0&baseamount=1099&transactionreference=1-2-345&orderreference=MyOrder123&currencyiso3a=GBP&errormessage=Payment+has+been+successfully+processed&settlestatus=0&jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NjExMDk1MDQsInBheWxvYWQiOnsicmVxdWVzdHJlZmVyZW5jZSI6IlcyMy10dzI5cWVyZSIsImp3dCI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUpwYzNNaU9pSnNhWFpsTWw5aGRYUnZhbmQwSWl3aWFXRjBJam94TlRZMU16UTJOVE01TGpjNE9UZ3dNVGdzSW5CaGVXeHZZV1FpT25zaVltRnpaV0Z0YjNWdWRDSTZJakV3TURBaUxDSmhZMk52ZFc1MGRIbHdaV1JsYzJOeWFYQjBhVzl1SWpvaVJVTlBUU0lzSW1OMWNuSmxibU41YVhOdk0yRWlPaUpIUWxBaUxDSnphWFJsY21WbVpYSmxibU5sSWpvaWRHVnpkREVpTENKc2IyTmhiR1VpT2lKbGJsOUhRaUo5ZlEuN3VWYUdkQkhJQjFQZ196aTBBOE9ZbVIwb0NfWWJaOGp0YWVSUXgxWXQtRSIsInZlcnNpb24iOiIxLjAwIiwicmVzcG9uc2UiOlt7IndhbGxldHNvdXJjZSI6IlZJU0FDSEVDS09VVCIsIndhbGxldGlkIjoiMTIzNDU2NzgiLCJ0cmFuc2FjdGlvbnN0YXJ0ZWR0aW1lc3RhbXAiOiIyMDE4LTA5LTI3IDE0OjE5OjAzIiwidG9rZW5pc2VkcGF5bWVudCI6IjAiLCJsaXZlc3RhdHVzIjoiMCIsImlzc3VlciI6IlRlc3QgSXNzdWVyIiwic3BsaXRmaW5hbG51bWJlciI6IjEiLCJkY2NlbmFibGVkIjoiMCIsInNldHRsZWR1ZWRhdGUiOiIyMDE4LTA5LTI3IiwiZXJyb3Jjb2RlIjoiMCIsImJhc2VhbW91bnQiOiIxMDk5IiwidGlkIjoiMjc4ODI3ODgiLCJtZXJjaGFudG51bWJlciI6IjAwMDAwMDAwIiwibWVyY2hhbnRjb3VudHJ5aXNvMmEiOiJHQiIsInRyYW5zYWN0aW9ucmVmZXJlbmNlIjoiMS0yLTM0NSIsIm1lcmNoYW50bmFtZSI6IlRlc3QgTWVyY2hhbnQiLCJwYXltZW50dHlwZWRlc2NyaXB0aW9uIjoiVklTQSIsIm9yZGVycmVmZXJlbmNlIjoiTXlPcmRlcjEyMyIsImFjY291bnR0eXBlZGVzY3JpcHRpb24iOiJFQ09NIiwiYWNxdWlyZXJyZXNwb25zZWNvZGUiOiIwMCIsInJlcXVlc3R0eXBlZGVzY3JpcHRpb24iOiJBVVRIIiwic2VjdXJpdHlyZXNwb25zZXNlY3VyaXR5Y29kZSI6IjAiLCJjdXJyZW5jeWlzbzNhIjoiR0JQIiwiYXV0aGNvZGUiOiJURVNUMjQiLCJlcnJvcm1lc3NhZ2UiOiJPayIsIm9wZXJhdG9ybmFtZSI6IndlYnNlcnZpY2VzQGV4YW1wbGUuY29tIiwic2VjdXJpdHlyZXNwb25zZXBvc3Rjb2RlIjoiMCIsIm1hc2tlZHBhbiI6IjQxMTExMSMjIyMjIzExMTEiLCJzZWN1cml0eXJlc3BvbnNlYWRkcmVzcyI6IjAiLCJpc3N1ZXJjb3VudHJ5aXNvMmEiOiJVUyIsInNldHRsZXN0YXR1cyI6IjAifV0sInNlY3JhbmQiOiJUIn19.nNZGIc8rN5ZnuAgzJs2-oDGPSdbeEMQXmFQlD-S_2yE",
                                "VISA_CANCEL_URL": "/?myBillAmount=&myBillName=&myBillEmail=&myBillTel=&errormessage=Payment+has+been+cancelled",
                                "APPLEPAY_SUCCESS_URL": "/?myBillAmount=&myBillName=&myBillEmail=&myBillTel=&errorcode=0&baseamount=200&transactionreference=23-9-141&orderreference=My_Order_123&eci=07&currencyiso3a=GBP&errormessage=Payment+has+been+successfully+processed&settlestatus=0&jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NjExMDk1MDQsInBheWxvYWQiOnsicmVxdWVzdHJlZmVyZW5jZSI6IlcyMy10dzI5cWVyZSIsImp3dCI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUpwYzNNaU9pSnNhWFpsTWw5aGRYUnZhbmQwSWl3aWFXRjBJam94TlRZMU16UTJOVE01TGpjNE9UZ3dNVGdzSW5CaGVXeHZZV1FpT25zaVltRnpaV0Z0YjNWdWRDSTZJakV3TURBaUxDSmhZMk52ZFc1MGRIbHdaV1JsYzJOeWFYQjBhVzl1SWpvaVJVTlBUU0lzSW1OMWNuSmxibU41YVhOdk0yRWlPaUpIUWxBaUxDSnphWFJsY21WbVpYSmxibU5sSWpvaWRHVnpkREVpTENKc2IyTmhiR1VpT2lKbGJsOUhRaUo5ZlEuN3VWYUdkQkhJQjFQZ196aTBBOE9ZbVIwb0NfWWJaOGp0YWVSUXgxWXQtRSIsInZlcnNpb24iOiIxLjAwIiwicmVzcG9uc2UiOlt7IndhbGxldHNvdXJjZSI6IkFQUExFUEFZIiwidHJhbnNhY3Rpb25zdGFydGVkdGltZXN0YW1wIjoiMjAxNy0xMS0wMiAxNDoyNDozMiIsImxpdmVzdGF0dXMiOiIwIiwic3BsaXRmaW5hbG51bWJlciI6IjEiLCJkY2NlbmFibGVkIjoiMCIsInNldHRsZWR1ZWRhdGUiOiIyMDE3LTExLTAyIiwiZXJyb3Jjb2RlIjoiMCIsImJhc2VhbW91bnQiOiIyMDAiLCJ0aWQiOiIyNzg4Mjc4OCIsIm1lcmNoYW50bnVtYmVyIjoiMDAwMDAwMDAiLCJtZXJjaGFudGNvdW50cnlpc28yYSI6IkdCIiwidHJhbnNhY3Rpb25yZWZlcmVuY2UiOiIyMy05LTE0MSIsIm1lcmNoYW50bmFtZSI6IlRlc3QgTWVyY2hhbnQiLCJwYXltZW50dHlwZWRlc2NyaXB0aW9uIjoiVklTQSIsIm9yZGVycmVmZXJlbmNlIjoiTXlfT3JkZXJfMTIzIiwiZWNpIjoiMDciLCJhY2NvdW50dHlwZWRlc2NyaXB0aW9uIjoiRUNPTSIsImNhdnYiOiJBcWpMU25BQXpWWE93c2ZBQmZPME1BQUNBQUE9IiwiYWNxdWlyZXJyZXNwb25zZWNvZGUiOiIwMCIsInJlcXVlc3R0eXBlZGVzY3JpcHRpb24iOiJBVVRIIiwic2VjdXJpdHlyZXNwb25zZXNlY3VyaXR5Y29kZSI6IjAiLCJjdXJyZW5jeWlzbzNhIjoiR0JQIiwiYXV0aGNvZGUiOiJURVNUODMiLCJlcnJvcm1lc3NhZ2UiOiJPayIsInNlY3VyaXR5cmVzcG9uc2Vwb3N0Y29kZSI6IjAiLCJtYXNrZWRwYW4iOiI0ODE4NTIjIyMjIyM1NDczIiwic2VjdXJpdHlyZXNwb25zZWFkZHJlc3MiOiIwIiwib3BlcmF0b3JuYW1lIjoid2Vic2VydmljZXNAZXhhbXBsZS5jb20iLCJzZXR0bGVzdGF0dXMiOiIwIn1dLCJzZWNyYW5kIjoiVCJ9fQ.D9WRCG_ilYhVNPxn_RoXccCmqshsoxfU0hbCQK-UQbU",
                                "APPLEPAY_ERROR_URL": "/?myBillAmount=&myBillName=&myBillEmail=&myBillTel=&errorcode=70000&transactionreference=42-2-81391&baseamount=1000&currencyiso3a=GBP&errormessage=Decline&settlestatus=3&jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NjExMDk1MDQsInBheWxvYWQiOnsicmVxdWVzdHJlZmVyZW5jZSI6Ilc0Mi1jN2swM3IwZSIsImp3dCI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUpwYzNNaU9pSnNhWFpsTWw5aGRYUnZhbmQwSWl3aWFXRjBJam94TlRZMU16UTJOVE01TGpjNE9UZ3dNVGdzSW5CaGVXeHZZV1FpT25zaVltRnpaV0Z0YjNWdWRDSTZJakV3TURBaUxDSmhZMk52ZFc1MGRIbHdaV1JsYzJOeWFYQjBhVzl1SWpvaVJVTlBUU0lzSW1OMWNuSmxibU41YVhOdk0yRWlPaUpIUWxBaUxDSnphWFJsY21WbVpYSmxibU5sSWpvaWRHVnpkREVpTENKc2IyTmhiR1VpT2lKbGJsOUhRaUo5ZlEuN3VWYUdkQkhJQjFQZ196aTBBOE9ZbVIwb0NfWWJaOGp0YWVSUXgxWXQtRSIsInZlcnNpb24iOiIxLjAwIiwicmVzcG9uc2UiOlt7IndhbGxldHNvdXJjZSI6IkFQUExFUEFZIiwidHJhbnNhY3Rpb25zdGFydGVkdGltZXN0YW1wIjoiMjAxOS0wNC0xOSAwODoxMDowMiIsImxpdmVzdGF0dXMiOiIwIiwic2V0dGxlZHVlZGF0ZSI6IjIwMTktMDQtMTkiLCJlcnJvcmNvZGUiOiI3MDAwMCIsInRpZCI6IjI3ODgyMjAwIiwibWVyY2hhbnRudW1iZXIiOiIxMTIyMzM0NCIsIm1lcmNoYW50Y291bnRyeWlzbzJhIjoiR0IiLCJ0cmFuc2FjdGlvbnJlZmVyZW5jZSI6IjQyLTItODEzOTEiLCJtZXJjaGFudG5hbWUiOiJUZXN0IG1lcmNoYW50IiwicGF5bWVudHR5cGVkZXNjcmlwdGlvbiI6IlZJU0EiLCJiYXNlYW1vdW50IjoiMTAwMCIsImFjY291bnR0eXBlZGVzY3JpcHRpb24iOiJFQ09NIiwiYWNxdWlyZXJyZXNwb25zZWNvZGUiOiIwNSIsInJlcXVlc3R0eXBlZGVzY3JpcHRpb24iOiJBVVRIIiwic2VjdXJpdHlyZXNwb25zZXNlY3VyaXR5Y29kZSI6IjEiLCJjdXJyZW5jeWlzbzNhIjoiR0JQIiwiYXV0aGNvZGUiOiI0Ni1ERUNMSU5FRCIsImVycm9ybWVzc2FnZSI6IkRlY2xpbmUiLCJvcGVyYXRvcm5hbWUiOiJsaXZlMl9hdXRvand0Iiwic2VjdXJpdHlyZXNwb25zZXBvc3Rjb2RlIjoiMCIsIm1hc2tlZHBhbiI6IjQwMDAwMCMjIyMjIzAwMDIiLCJzZWN1cml0eXJlc3BvbnNlYWRkcmVzcyI6IjAiLCJpc3N1ZXJjb3VudHJ5aXNvMmEiOiJaWiIsInNldHRsZXN0YXR1cyI6IjMifV0sInNlY3JhbmQiOiJvWU9rcURDZnZNIn19.0zyWHsDob945k12LW5HFY2zu9TSRKjNuqmJ3KWsZPFQ",
                                "APPLEPAY_CANCEL_URL": "/?myBillAmount=&myBillName=&myBillEmail=&myBillTel=&errorcode=%5Bobject+Object%5D&errormessage=Payment+has+been+cancelled"})
    }

    return AttrDict(test_data_dict)


TEST_DATA = load_test_data()


class TestData:

    def __init__(self, config__test):
        self._base_page = config__test.base_page

        """ User section """
        self.step_payment_cardinal_url = TEST_DATA.STEP_PAYMENT.CARDINAL_URL
        self.step_payment_visa_success_url = TEST_DATA.STEP_PAYMENT.VISA_SUCCESS_URL
        self.step_payment_visa_cancel_url = TEST_DATA.STEP_PAYMENT.VISA_CANCEL_URL
        self.step_payment_apple_pay_success_url = TEST_DATA.STEP_PAYMENT.APPLEPAY_SUCCESS_URL
        self.step_payment_apple_pay_error_url = TEST_DATA.STEP_PAYMENT.APPLEPAY_ERROR_URL
        self.step_payment_apple_pay_cancel_url = TEST_DATA.STEP_PAYMENT.APPLEPAY_CANCEL_URL
