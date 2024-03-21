const BASE_URL = "http://127.0.0.1:4321";

$(document).ready(function () {
  // Ajax post request
  $("#pred-form").submit(function (e) {
    e.preventDefault();

    console.log("Ajax");

    // Serialize form data
    let formData = $(this).serialize();

    console.log(formData);

    // Submit form using Ajax
    //   $.ajax({
    //     type: 'POST',
    //     url: BASE_URL + '/predict', // URL
    //     data: formData,
    //     success: function(response){
    //       $('#pred-res').html(response); // response from server
    //     },
    //     error: function(){
    //       $('#response').html("Error submitting form."); // error message
    //     }
    //   });

    $('#pred-res').addClass('text-success');
    $('#pred-res').html('$1000');
  });


  // fill the neighborhood options
  let neighbors = [
    'Wallingford', 'Georgetown', 'Fairmount Park', 'Whittier Heights',
  'Sunset Hill', 'Eastlake', 'Fremont', 'Green Lake', 'Portage Bay',
  'Phinney Ridge', 'Crown Hill', 'Columbia City', 'Lawton Park',
  'North Queen Anne', 'West Queen Anne', 'First Hill', 'Broadway',
  'Stevens', 'North Admiral', 'International District',
  'North Beacon Hill', 'West Woodland', 'Greenwood', 'Cedar Park',
  'Mount Baker', 'Mann', 'Ravenna', 'Belltown',
  'University District', 'Harrison/Denny-Blaine', 'South Delridge',
  'Atlantic', 'Broadview', 'Maple Leaf', 'East Queen Anne',
  'Pioneer Square', 'Highland Park', 'Laurelhurst', 'Haller Lake',
  'Madison Park', 'Fauntleroy', 'Madrona', 'Loyal Heights',
  'Gatewood', 'Leschi', 'Westlake', 'Adams',
  'North Beach/Blue Ridge', 'North Delridge', 'Bryant',
  'Seward Park', 'View Ridge', 'Central Business District',
  'Pike-Market', 'High Point', 'Yesler Terrace', 'Alki',
  'Bitter Lake', 'Lower Queen Anne', 'Harbor Island', 'Windermere',
  'Minor', 'Rainier Beach', 'Victory Heights', 'Seaview',
  'Roosevelt', 'Dunlap', 'Matthews Beach', 'Southeast Magnolia',
  'Genesee', 'Olympic Hills', 'Mid-Beacon Hill', 'Brighton',
  'Interbay', 'Briarcliff', 'Montlake', 'North College Park',
  'Riverview', 'Pinehurst', 'Wedgwood', 'Meadowbrook',
  'Rainier View', 'South Beacon Hill', 'Industrial District',
  'South Park', 'South Lake Union', 'Roxhill', 'Arbor Heights',
  'Holly Park'
  ];

  neighbors.sort();
  
  $.each(neighbors, function(index, option) {
    $('#form-neighbourhood').append($('<option>', {
      value: option,
      text: option
    }));
  });

});
  
