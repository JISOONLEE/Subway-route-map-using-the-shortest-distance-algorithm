package com.example.demo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class subwayController {
	
	@RequestMapping(value="Subway_route", method = RequestMethod.POST)
	public String subway_route(@RequestParam("start")String start, @RequestParam("start_line")int start_line, @RequestParam("finish")String finish, 
			@RequestParam("finish_line")int finish_line, @RequestParam("developer")String developer, Model model)
	{
		String start_info = start+Integer.toString(start_line);
		String finish_info = finish + Integer.toString(finish_line);
		String str = null;
		System.out.println(start_info);
		System.out.println(finish_info);
		System.out.println(developer);
		
		//C:\Users\이지순\AppData\Local\conda\conda\envs\tutorial\python.exe
		//C:\Users\이지순\PycharmProjec7ts\Shortest_distance_project\Dijkstra_Subway.py
		//%windir%\System32\cmd.exe "/K" C:\ProgramData\Anaconda3\Scripts\activate.bat C:\ProgramData\Anaconda3
		
		switch (developer) {
			case "jisoon_dijkstra":
				ProcessBuilder pa = new ProcessBuilder("C:\\Users\\***\\AppData\\Local\\conda\\conda\\envs\\tutorial\\python.exe", 
						"C:\\Users\\***\\PycharmProjects\\Shortest_distance_project\\Dijkstra_Subway.py", start_info, finish_info);
				try {
					Process p = pa.start();
					BufferedReader bf = new BufferedReader(new InputStreamReader(p.getInputStream()));
					String s = bf.readLine();
					String route[] = s.split("a");
					for(int i=0;i<route.length;i++)
					{
						System.out.println(route[i]);
					}
					model.addAttribute("start", Integer.toString(start_line)+"호선 "+start+"역");
					model.addAttribute("finish", Integer.toString(finish_line)+"호선 "+finish+"역");
					model.addAttribute("developer", "개발자1");
					model.addAttribute("algorithm", "Dijkstra");
					model.addAttribute("route", route[0]);
					model.addAttribute("distance", route[1]);
					
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;
			case "jisoon_floyd":
				ProcessBuilder pb = new ProcessBuilder("C:\\Users\\***\\AppData\\Local\\conda\\conda\\envs\\tutorial\\python.exe", 
						"C:\\Users\\***\\PycharmProjects\\Shortest_distance_project\\FloydWarshall_Subway.py", start_info, finish_info);
				try {
					Process p2 = pb.start();
					BufferedReader bf2 = new BufferedReader(new InputStreamReader(p2.getInputStream()));
					String s2 = bf2.readLine();
					String route2[] = s2.split("a");
					for(int i=0;i<route2.length;i++)
					{
						System.out.println(route2[i]);
					}
					model.addAttribute("start", Integer.toString(start_line)+"호선 "+start+"역");
					model.addAttribute("finish", Integer.toString(finish_line)+"호선 "+finish+"역");
					model.addAttribute("developer", "개발자1");
					model.addAttribute("algorithm", "FloydWarshall");
					model.addAttribute("route", route2[0]);
					model.addAttribute("distance", route2[1]);
					
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;
		}
		
		return "subway_route";
	}
}
