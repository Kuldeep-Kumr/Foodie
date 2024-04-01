import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import {AppModule} from './app.modules'
import { provideHttpClient, withFetch} from '@angular/common/http';
import { routes } from './app.routing.module';
import { provideClientHydration } from '@angular/platform-browser';

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes), AppModule, provideClientHydration(),provideHttpClient(withFetch())]
};
