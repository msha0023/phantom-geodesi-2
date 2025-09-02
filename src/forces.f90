module forces
 implicit none
contains

!----------------------------------------------------------------
!+
!
!  calculate gravitational acceleration on each particle
!
!+
!----------------------------------------------------------------
subroutine get_newtonian_force_new(np,xall,vall,fterm_new,mall,i)
  use utils_gr,     only: get_u0

  real, dimension(:,:), intent(in) :: xall,vall
  real, dimension(:), intent(in) :: mall
  integer, intent(in) :: np,i
  real, dimension(3), intent(inout) :: fterm_new
  real, dimension(3) :: x,x_other,x_rel,v
  real :: rr,ddr,v_mag
  real    :: U0
  integer :: j

  ! we determine the force on each particle
  x = xall(:,i)
  v = vall(:,i)
  call get_u0(x,v,U0)
  do j = 1,np
    if (i .ne. j) then
      ! determine relative position
      x_other = xall(:,j)
      x_rel = x - x_other
      rr = sqrt(dot_product(x_rel,x_rel))
      v_mag = sqrt(dot_product(v,v))

      ddr = 1.0 / rr**3
      ! determine the force components in vector form
      fterm_new(:) = fterm_new(:) - ddr*x_rel*mall(j)
      ! fterm_new(:) = fterm_new(:) - (U0)*ddr*x_rel*mall(j)
      ! fterm_new(:) = fterm_new(:) - U0*(1. + v_mag**2)*ddr*x_rel*mall(j)

    endif
  enddo

end subroutine get_newtonian_force_new

end module forces
