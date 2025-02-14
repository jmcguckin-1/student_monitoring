import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {TestServiceService} from './test-service.service';
import { CommonModule } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  providers: [TestServiceService]
})
export class AppComponent implements OnInit{
  dataClass: any;
  constructor(private testService: TestServiceService) {

  }
  ngOnInit(): void {

    this.testService.fetchClassData().subscribe(data => {
        this.testService.setData(data);
        this.dataClass = this.testService.getData();
      }
    )

  }
  title = 'frontend';


}
