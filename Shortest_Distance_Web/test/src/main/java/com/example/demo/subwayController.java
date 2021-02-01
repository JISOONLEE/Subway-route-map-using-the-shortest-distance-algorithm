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
		String info = Integer.toString(start_line)+"a"+start+"a"+Integer.toString(finish_line)+"a"+finish;
		System.out.println(developer);
		
		System.out.println(info);
		String s = "";
		String dev = "";
		String algo = "";
		
		switch (developer) {
			case "dev1_dijkstra":
				dev = "개발자1";
				algo = "다익스트라";
				ProcessBuilder pa = new ProcessBuilder("Python Path"+"\\AppData\\Local\\conda\\conda\\envs\\tutorial\\python.exe", 
						"Python File Path" + "\\Dijkstra_Subway.py", info);
				try {
					Process p = pa.start();
					BufferedReader bf = new BufferedReader(new InputStreamReader(p.getInputStream()));
					s = bf.readLine();
					
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;
			case "dev1_floyd":
				dev = "개발자1";
				algo = "플로이드 와샬";
				ProcessBuilder pb = new ProcessBuilder("Python Path"+"\\AppData\\Local\\conda\\conda\\envs\\tutorial\\python.exe", 
						"Python File Path" + "FloydWarshall_Subway.py", info);
				try {
					Process p2 = pb.start();
					BufferedReader bf2 = new BufferedReader(new InputStreamReader(p2.getInputStream()));
					s = bf2.readLine();
					
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;
			case "dev2_dijkstra":
				dev = "개발자2";
				algo = "다익스트라";
				ProcessBuilder pc = new ProcessBuilder("Python Path"+"\\AppData\\Local\\conda\\conda\\envs\\tutorial\\python.exe", 
						"Python File Path" + "\\Dijkstra_Searching_SubwayRoute.py", info);
				try {
					Process p3 = pc.start();
					BufferedReader bf3 = new BufferedReader(new InputStreamReader(p3.getInputStream(), "euc-kr"));
					s = bf3.readLine();
					
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;
			case "dev2_spfa":
				dev = "개발자2";
				algo = "SPFA";
				ProcessBuilder pd = new ProcessBuilder("Python Path"+"\\AppData\\Local\\conda\\conda\\envs\\tutorial\\python.exe", 
						"Python File Path" + "\\SPFA_Searching_SubwayRoute.py", info);
				try {
					Process p4 = pd.start();
					BufferedReader bf4 = new BufferedReader(new InputStreamReader(p4.getInputStream(), "euc-kr"));
					s = bf4.readLine();
					
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;
		}
		
		String route[] = s.split("a");
		for(int i=0;i<route.length;i++)
		{
			System.out.println(route[i]);
		}
		model.addAttribute("start", Integer.toString(start_line)+"호선 "+start+"역");
		model.addAttribute("finish", Integer.toString(finish_line)+"호선 "+finish+"역");
		model.addAttribute("developer", dev);
		model.addAttribute("algorithm", algo);
		model.addAttribute("route", route[0]);
		model.addAttribute("distance", route[1]);
		model.addAttribute("transfer", route[2]);
		
		return "subway_route";
	}
}
