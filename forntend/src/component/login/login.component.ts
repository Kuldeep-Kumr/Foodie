import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../service/auth.service';
import { environment } from '../../environments/environment';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

  user = {
    username: '',
    password: ''
  };
  errorMessage: string = '';
  token: string = '';
  constructor(private authService: AuthService, private router: Router) { };
  login(loginForm: NgForm) {
    if (loginForm.valid) {
      this.authService.post(environment.domain + environment.loginUrl, this.user).subscribe(
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
