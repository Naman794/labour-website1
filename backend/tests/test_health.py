import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_healthz():
    client = APIClient()
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.data["status"] == "ok"


@pytest.mark.django_db
def test_otp_bypass_and_me(settings):
    settings.DEV_OTP_BYPASS = True
    client = APIClient()
    phone_number = "+15550001111"

    request_response = client.post(
        "/auth/request-otp",
        {"phone_number": phone_number},
        format="json",
    )
    assert request_response.status_code == 200
    otp = request_response.data["otp"]

    verify_response = client.post(
        "/auth/verify-otp",
        {"phone_number": phone_number, "otp": otp},
        format="json",
    )
    assert verify_response.status_code == 200

    access = verify_response.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
    me_response = client.get("/api/me")
    assert me_response.status_code == 200
    assert me_response.data["phone_number"] == phone_number
