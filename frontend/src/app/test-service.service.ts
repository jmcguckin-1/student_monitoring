import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TestServiceService {

  constructor(private http: HttpClient) { }
  private classData = [];
  private nameData = [];
  private className = "";
  private report = [];
  private chosenStudent = "";
  private currentComment = "";
  options: any;
  setData (x: any){
    this.classData = x;
  }

  getData(){
    return this.classData;
  }

  setComment(x:any){
    this.currentComment = x;
  }

  getCurrentStudent(){
    return this.chosenStudent;
  }

  addComment(){
        this.options = {name: this.chosenStudent, class_name: this.className, comment: this.currentComment};
        console.log(this.options);
    return this.http.post<any>('/api/add_comment', this.options);
  }

  getNames(){
    return this.nameData;
  }

  setNames(x:any){
    this.nameData = x;
  }

  setReport(x:any){
    this.report = x;
  }

  getReport(){
    return this.report;
  }

   setClass(x:any){
    this.className = x;
    this.options = { params: new HttpParams().set('name', this.className) };
  }

  setStudent(x:any){
    this.chosenStudent = x;
  }

  getStudentData(){
    return this.classData[0]['students'];
  }
 fetchClassData(): Observable<any> {
    return this.http.get<any>('/api/get_class', this.options);
}

 fetchReport(): Observable<any> {
    this.options = { params: new HttpParams()
        .set('name', this.chosenStudent)
        .set('class_name', this.className)};
    return this.http.get<any>('/api/get_attendance_file', this.options);
}

 fetchBehaviourReport(): Observable<any> {
    this.options = { params: new HttpParams()
        .set('name', this.chosenStudent)
        .set('class_name', this.className)};
    return this.http.get<any>('/api/get_behaviour_file', this.options);
}

sendAttendance(x:any): Observable<any> {
    this.options = { list: x, name: this.className };
    return this.http.post<any>('/api/update_class', this.options);
}

 fetchNames(): Observable<any> {
    return this.http.get<any>('/api/get_names');
}

addBehaviour(behaviour:any ,comments:any): Observable<any>{
    this.options = { class_name: this.className, behaviour: behaviour,
      comments: comments, date: this.classData[0]['date'] };
    return this.http.post<any>("/api/add_behaviour", this.options);
}
}
