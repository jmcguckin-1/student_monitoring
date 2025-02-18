import {Component, ElementRef, OnInit} from '@angular/core';
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
  studentList: any;
  namesList : any;
  attendanceList: any = [];
  constructor(private testService: TestServiceService) {

  }
  ngOnInit(): void {

    this.testService.fetchNames().subscribe(data => {
        this.testService.setNames(data);
        this.namesList = this.testService.getNames();
    })

  }

  addElement(event:any){
    this.attendanceList.push(event.target.value);
  }

  sendAttendance(){
    this.testService.sendAttendance(this.attendanceList).subscribe(data => {
      console.log("success");
    });
  }

  setClass(x: any){
    this.testService.setClass(x);
      this.testService.fetchClassData().subscribe(data => {
        this.testService.setData(data);
        this.dataClass = this.testService.getData();
        this.studentList = this.testService.getStudentData();
      }
    )
  }
  title = 'frontend';


}
