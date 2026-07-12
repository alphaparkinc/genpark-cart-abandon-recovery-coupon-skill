class CartAbandonRecoveryCouponClient:
    def get_coupon(self, reason_code: str, cart_subtotal: float) -> dict:
        return {"suggested_coupon_code": "RECOVER15" if reason_code == "pricing" else "FREESHIP"}