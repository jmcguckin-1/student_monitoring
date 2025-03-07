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
  private fullReport = [];
  private currentAssignment = "";
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

  getStudentReportName(){
    return this.fullReport[0][0]["student_name"];
  }

  getOverallAttendance(){
    return this.fullReport[0][0]["attendance"];
  }

  setAssignment(x:any){
    if (x !== ''){
      this.currentAssignment = x;
    }
  }

  getGradesCommentList(){
    let list : any = [];
    for (let i=1; i<3; i++) {
      list.push(this.fullReport[0][i]);
    }
    return list;
  }

  addComment(){
        this.options = {name: this.chosenStudent, class_name: this.className, comment: this.currentComment};
        return this.http.post<any>('/api/add_comment', this.options);
  }

  getFullReport(){
     this.options = { params: new HttpParams().set('name', this.chosenStudent) };
     return this.http.get<any>("api/get_full_report", this.options);
  }

   markAssignment(mark:any, comment:any, assignment:any){
    this.options = {name: this.chosenStudent, class_name: this.className, comment: comment,
    assignment: assignment, mark: mark};
        return this.http.post<any>('/api/set_grade', this.options);
  }

  getAssignmentNames(){
      this.options = { params: new HttpParams().set('class_name', this.className) };
     return this.http.get<any>("api/get_assignment_names", this.options);
  }

  hasStudentSubmitted(){
      this.options = { params: new HttpParams().set('class_name', this.className)
          .set("name", this.chosenStudent)
          .set("assignment", this.currentAssignment)};
     return this.http.get<any>("api/has_student_submitted", this.options);
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

setFullReport(x:any){
    this.fullReport = x;
}
}
