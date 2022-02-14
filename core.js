Vue.createApp({
    data() {
        const titles = {main: {text: "Austen C. Myers"}, sub:{text: "Resume"}}

        const links = [
            {text: 'Github', url: 'https://github.com/austenc-id'},
            {text: 'Linkdin', url: ''},
            ]
        const sections = [
            {title: "Work History", entries: [
                {
                    title: "Biomedical Equipment Technician",
                    org: "Idaho Army National Guard",
                    dates: {
                        start: "July 2019",
                        end: "December 2021"
                    },
                },
                {
                    title: "Combat Medic",
                    org: "Idaho Army National Guard",
                    dates: {
                        start: "March 2017",
                        end: "December 2021"
                    },
                },
                {
                    title: "Global Technical Support",
                    org: "Verizon Wireless",
                    dates: {
                        start: "January 2017",
                        end: "July 2018"
                    },
                },
                {
                    title: "Bartender",
                    org: "Sun Valley Company",
                    dates: {
                        start: "June 2016",
                        end: "December 2016"
                    },
                },
                {
                    title: "Barista",
                    org: "Kimo Bean Coffee Co",
                    dates: {
                        start: "October 2015",
                        end: "May 2016"
                    },
                },
                {
                    title: "Server",
                    org: "Buffalo Wild Wings",
                    dates: {
                        start: "October 2014",
                        end: "October 2015"
                    },
                },
                {
                    title: "Barista",
                    org: "Starbucks",
                    dates: {
                        start: "April 2014",
                        end: "January 2015"
                    },
                },

            ]
        },
            {
                title: "Education", entries: [
                    {
                        title: "Full Stack Django",
                        org: "Portland Code Guild",
                        dates: {
                            start: "October 2021",
                            end: "February 2022"
                        },
                        completed: "not yet"
                    },
                    {
                        title: "Biomedical Equpiment Technician School",
                        org: "DoD Medical Education & Training Campus",
                        dates: {
                            start: "July 2019",
                            end: "June 2020"
                        },
                        completed: true
                    },
                    {
                        title: "Combat Medic School",
                        org: "DoD Medical Education & Training Campus",
                        dates: {
                            start: "November 2017",
                            end: "May 2018"
                        },
                        completed: true
                    },
                    {
                        title: "Associate's in Liberal Arts",
                        org: "Leeward Community College",
                        dates: {
                            start: "July 2015",
                            end: "May 2016"
                        },
                        completed: false
                    },
                    {
                        title: "Bachelor's in Geography and GPS Technology",
                        org: "University of Northern Colorado",
                        dates: {
                            start: "July 2012",
                            end: "March 2014"
                        },
                        completed: false
                    },
            ]},
            {title: "Skills"},
        ]
      return {
        titles: titles,
        links: links,
        content: sections
      };
    },
  }).mount("#VUE");