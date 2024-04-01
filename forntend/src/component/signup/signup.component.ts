import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../service/auth.service';
import { environment } from '../../environments/environment';
import { stringify } from 'querystring';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrl: './signup.component.css'
})
export class SignupComponent {
  userData: any = {
    name: '',
    email: '',
    phone: '',
    password: '',
    confirmPassword: '',
    is_owner: false,
    img_url: '',
    restaurant_name: '',
    location: '',
    cuisine: ''
  };
  errorMessage=''
  constructor(private authService: AuthService, private router: Router) { };
  validatePassword(): boolean {
    if (this.userData.password != this.userData.confirmPassword) {
      return false
    }
    return true
  }
  validatePhone(): boolean {
    if ((this.userData.phone).length!=10) {
      return false
    }
    return true
  }
  signUp(signupForm: NgForm) {
    if (signupForm && this.validatePassword() && this.validatePhone()) {
      this.authService.post(environment.domain + environment.singupUrl, this.userData).subscribe(
        (response) => {
          if (response && response.token) {
            sessionStorage.setItem('token', response.token)
            if (response.is_owner) {
              this.router.navigate(['/owner/home'])
            }
            else {
              this.router.navigate(['/user/home'])
            }

          }
        },
        (error) => {
          this.errorMessage = error.error.message;
          console.log("Error logging in:", this.errorMessage)
        }
      )
    }
  }
}
