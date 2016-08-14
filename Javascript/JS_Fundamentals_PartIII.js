function personConstructor(person) {
	data = {
		name: person,
		distance_traveled: 0,
		say_name: function() {
			console.log(data.name);
			return data;
		},
		say_something: function(str) {
			console.log(data.name + " says '" + str + "'");
			return data;
		},
		walk: function() {
			console.log(data.name + " is walking..");
			data.distance_traveled += 3;
			return data;
		},
		fly: function() {
			console.log(data.name + " is flying on his broom..");
			data.distance_traveled += 10;
			return data;
		},
		crawl: function() {
			console.log(data.name + " is crawling..");
			data.distance_traveled += 1;
			return data;
		}
	}
	return data
}
person_1 = personConstructor('Harry');
person_1.say_name().say_something('Expelliarmus!').fly().fly().crawl().fly().walk();
console.log(person_1.distance_traveled);


function wizardConstructor(wizard) {
	data = {
		name: wizard,
		school: 'Hogwarts',
		year_level: "First-Year",
		levelUp: function(){
			if (data.year_level == "First-Year") {
				console.log('You been promoted to Second-Year!');
				data.year_level = "Second-Year";
			} else if (data.year_level == "Second-Year") {
				console.log('You been promoted to Third-Year!');
				data.year_level = "Third-Year";
			} else if (data.year_level == "Third-Year") {
				console.log('You been promoted to Fourth-Year!');
				data.year_level = "Fourth-Year";
			} else if (data.year_level == "Fourth-Year") {
				console.log('You been promoted to Fifth-Year!');
				data.year_level = "Fifth-Year";
			} else {
				console.log('Congrats! You have passed all your OWL Exams and Graduated from Hogwarts!');
			}
			return data;
		}
	}
	return data;
}
wizard_1 = wizardConstructor('Harry Potter');
wizard_1.levelUp().levelUp().levelUp().levelUp().levelUp();
console.log(wizard_1.year_level);
