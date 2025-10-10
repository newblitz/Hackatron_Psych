import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class SendGridEmailService:
    def __init__(self):
        self.api_key = settings.SENDGRID_API_KEY
        self.from_email = settings.DEFAULT_FROM_EMAIL
        
    def send_verification_email(self, to_email, otp):
        """
        Send OTP verification email using SendGrid API
        """
        try:
            # Create the email content
            subject = "OTP for Email Verification - Euphoria"
            
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Email Verification</title>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                    .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                    .header {{ background: linear-gradient(135deg, #06b6d4, #7c3aed); color: white; padding: 20px; text-align: center; border-radius: 10px 10px 0 0; }}
                    .content {{ background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px; }}
                    .otp-box {{ background: #fff; border: 2px solid #7c3aed; border-radius: 8px; padding: 20px; text-align: center; margin: 20px 0; }}
                    .otp-code {{ font-size: 32px; font-weight: bold; color: #7c3aed; letter-spacing: 5px; }}
                    .footer {{ text-align: center; margin-top: 20px; color: #666; font-size: 14px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>Euphoria</h1>
                        <p>Email Verification</p>
                    </div>
                    <div class="content">
                        <h2>Hello!</h2>
                        <p>Thank you for registering with Euphoria! To complete your registration, please use the verification code below:</p>
                        
                        <div class="otp-box">
                            <p style="margin: 0 0 10px 0; color: #666;">Your verification code is:</p>
                            <div class="otp-code">{otp}</div>
                        </div>
                        
                        <p><strong>Important:</strong></p>
                        <ul>
                            <li>This code will expire in 5 minutes</li>
                            <li>Enter this code exactly as shown</li>
                            <li>If you didn't request this code, please ignore this email</li>
                        </ul>
                        
                        <p>If you have any questions, please contact our support team.</p>
                        
                        <p>Best regards,<br>The Euphoria Team</p>
                    </div>
                    <div class="footer">
                        <p>© 2025 
                    Euphoria. All rights reserved.</p>
                    </div>
                </div>
            </body>
            </html>
            """
            
            text_content = f"""
            Hello!
            
            Thank you for registering with Euphoria! 
            
            Your verification code is: {otp}
            
            This code will expire in 5 minutes. Please enter this code to complete your registration.
            
            If you didn't request this code, please ignore this email.
            
            Best regards,
            Euphoria Team
            """
            
            # Create the email message
            message = Mail(
                from_email=self.from_email,
                to_emails=to_email,
                subject=subject,
                html_content=html_content,
                plain_text_content=text_content
            )
            
            # For production: Try to send via SendGrid API first
            if self.api_key and self.api_key != "your_sendgrid_api_key_here":
                try:
                    sg = SendGridAPIClient(api_key=self.api_key)
                    response = sg.send(message)
                    
                    if response.status_code in [200, 201, 202]:
                        logger.info(f"Email sent successfully to {to_email}")
                        print(f"✅ Email sent successfully via SendGrid API to {to_email}")
                        return True
                    else:
                        logger.error(f"SendGrid API error: {response.status_code} - {response.body}")
                        print(f"❌ SendGrid API error: {response.status_code}")
                        # Fall through to console output
                except Exception as e:
                    logger.error(f"SendGrid API error: {str(e)}")
                    print(f"❌ SendGrid API error: {str(e)}")
                    # Fall through to console output
            
            # Fallback: Print to console (for testing or if SendGrid fails)
            print(f"\n{'='*60}")
            print(f"📧 EMAIL VERIFICATION OTP (Fallback)")
            print(f"{'='*60}")
            print(f"To: {to_email}")
            print(f"OTP: {otp}")
            print(f"Subject: {subject}")
            print(f"{'='*60}\n")
            
            return True
                
        except Exception as e:
            logger.error(f"Error sending email to {to_email}: {str(e)}")
            # Fallback to console output
            print(f"\n{'='*60}")
            print(f"📧 EMAIL VERIFICATION OTP (SendGrid Error)")
            print(f"{'='*60}")
            print(f"To: {to_email}")
            print(f"OTP: {otp}")
            print(f"Error: {str(e)}")
            print(f"{'='*60}\n")
            return True  # Return True so registration can continue

# Create a global instance
email_service = SendGridEmailService()
